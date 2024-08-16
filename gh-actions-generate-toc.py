# This file is used to generate a table of released instruments with GitHub Actions
# This should be run with GitHub Actions

import boto3
import os
import re
import requests
import sys
import urllib.parse


instruments = {}
instrument_urls = {}
download_size = {}

# Retrieve file list from GitHub Releases

repo = os.environ["GITHUB_REPOSITORY"]
api_url = f"https://api.github.com/repos/{repo}/releases?per_page=100&page="
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
    "X-GitHub-Api-Version": "2022-11-28",
}
releases = []
page = 1
while True:
    response = requests.get(api_url + str(page), headers=headers)
    if not 200 <= response.status_code < 300:
        raise Exception(f"GET request failed with status code {response.status_code}")
    page_release = response.json()
    if len(page_release) == 0:
        break
    releases += page_release
    page += 1

for release in releases:
    if " - " not in release["name"]:
        continue
    catagory, name = release["name"].split(" - ", 1)
    if catagory not in instruments:
        instruments[catagory] = {}
        instrument_urls[catagory] = {}
        download_size[catagory] = {}
    assert name not in instruments[catagory], f"Duplicate instrument name {name} in catagory {catagory}"
    instruments[catagory][name] = {}
    instrument_urls[catagory][name] = release["html_url"]
    download_size[catagory][name] = {}
    for asset in release["assets"]:
        instruments[catagory][name][re.sub(r"[\[\]_]", lambda m: f"\\{m[0]}", asset["name"].replace("\\", "\\\\"))] = (
            asset["browser_download_url"]
        )
        download_size[catagory][name][
            re.sub(r"[\[\]_]", lambda m: f"\\{m[0]}", asset["name"].replace("\\", "\\\\"))
        ] = asset["size"]

try:
    with open("instruments.md", mode="rt", encoding="utf-8") as f:
        old_markdown = f.read()
except FileNotFoundError:
    old_markdown = ""


# Retrieve file list from S3

download_url_prefix = os.environ["DOWNLOAD_URL_PREFIX"]
endpoint_url = os.environ["ENDPOINT_URL"]
access_key = os.environ["ACCESS_KEY"]
secret_key = os.environ["SECRET_KEY"]
bucket_name = os.environ["BUCKET_NAME"]

s3 = boto3.client(
    "s3", endpoint_url=endpoint_url, aws_access_key_id=access_key, aws_secret_access_key=secret_key, verify=True
)

objects = s3.list_objects_v2(Bucket=bucket_name, MaxKeys=1000000)["Contents"]
for i in objects:
    parts = i["Key"].split("/")
    if len(parts) < 3 or parts[-1] == "":
        continue
    catagory = parts[1]
    name = parts[2]
    if len(parts) == 3:
        name = name.split(".", 1)[0]
    if catagory not in instruments:
        instruments[catagory] = {}
    if name not in instruments[catagory]:
        instruments[catagory][name] = {}
    if name not in download_size[catagory]:
        download_size[catagory][name] = {}
    filename = re.sub(
        r"[\[\]_]", lambda m: f"\\{m[0]}", (i["Key"].rsplit("/", 1)[1] + " (CloudFlare)").replace("\\", "\\\\")
    )
    instruments[catagory][name][filename] = urllib.parse.urljoin(download_url_prefix, urllib.parse.quote(i["Key"]))
    download_size[catagory][name][filename] = i["Size"]


# Generate markdown


def human_readable_size(size):
    for unit in ["B", "KiB", "MiB", "GiB", "TiB", "PiB"]:
        if size < 20480:
            return f"{size:.5g} {unit}"
        size /= 1024


markdown = "# Instrument List\n\n"

markdown += (
    "Instrument files are hosted on GitHub and CloudFlare. If a same file is available on both platforms, "
    "the CloudFlare link is recommended. It's faster and you won't need to rename understrike "
    "(`_`) to space after downloading.\n\n"
    "## About File Types\n\n"
    "- `*.sts.7z`: Compressed original sample files extracted from the sts file. Audio files are in opus format.\n"
    "- `*.sf2`: Converted SF2 format soundfont file.\n"
    "- `*.sf3`: Converted SF3 format soundfont file.\n"
    "- `*.sfz.7z`: Compressed original SFZ files. May not standard SFZ format and can't be loaded by SFZ player.\n"
    "- `sfz+flac.zip`: Converted SFZ files with FLAC audio files. You can use it directly in SFZ player.\n"
)

for catagory in sorted(instruments.keys()):
    markdown += f"## {catagory}\n\n"
    for name in sorted(instruments[catagory].keys()):
        if catagory in instrument_urls and name in instrument_urls[catagory]:
            markdown += f"- [{name}]({instrument_urls[catagory][name]})\n"
        else:
            markdown += f"- {name}\n"
        for asset in sorted(instruments[catagory][name].keys(), key=lambda x: x.rsplit(".", 1)[1]):
            markdown += (
                f"  - [{asset}]({instruments[catagory][name][asset]}) "
                f"({human_readable_size(download_size[catagory][name][asset])})\n"
            )
    markdown += "\n"

print("Generated markdown:", file=sys.stderr)
print(markdown)

# Only write the file if the contents have changed
if markdown != old_markdown:
    os.system('echo "continue_commit=true" >> "$GITHUB_OUTPUT"')
    with open("instruments.md", mode="wt", encoding="utf-8") as f:
        f.write(markdown)
    # Find out what instrument changed to set commit message
    old_markdown_insts = dict((i[1], i[0]) for i in re.findall(r"(- \[(.*)\].*\r?\n(  - .*\r?\n?)*)", old_markdown))
    new_markdown_insts = dict((i[1], i[0]) for i in re.findall(r"(- \[(.*)\].*\r?\n(  - .*\r?\n?)*)", markdown))
    added = set(new_markdown_insts.keys()) - set(old_markdown_insts.keys())
    removed = set(old_markdown_insts.keys()) - set(new_markdown_insts.keys())
    modified = {}
    for i in set(new_markdown_insts.keys()) & set(old_markdown_insts.keys()):
        links_old = dict((j[1], j[0]) for j in re.findall(r"\[(.*?)\]\((.*?)\)", old_markdown_insts[i]))
        links_new = dict((j[1], j[0]) for j in re.findall(r"\[(.*?)\]\((.*?)\)", new_markdown_insts[i]))
        if links_old != links_new:
            modified[i] = (links_old, links_new)
    message = "Update Instrument Table of Contents\n"
    if added:
        message += "Added: " + ", ".join(added) + "\n"
    if removed:
        message += "Removed: " + ", ".join(removed) + "\n"
    if modified:
        message += "Modified: \n"
        for i in modified:
            message += "  " + i + "\n"
            for j in set(modified[i][0].keys()) | set(modified[i][1].keys()):
                if j not in modified[i][0]:
                    message += "    Added: " + modified[i][1][j] + "\n"
                elif j not in modified[i][1]:
                    message += "    Removed: " + modified[i][0][j] + "\n"
                elif modified[i][0][j] != modified[i][1][j]:
                    message += f"    Renamed: {modified[i][0][j]} -> {modified[i][1][j]}\n"
    print("-" * 80)
    print("Commit message:")
    print(message)
    delimiter = "EOF"
    while delimiter in message:
        delimiter += "EOF"
    os.system(f'echo "commit_message<<{delimiter}" >> "$GITHUB_OUTPUT"')
    for line in message.split("\n"):
        os.system(f'echo "{line}" >> "$GITHUB_OUTPUT"')
    os.system(f'echo "{delimiter}" >> "$GITHUB_OUTPUT"')
else:
    os.system('echo "continue_commit=false" >> "$GITHUB_OUTPUT"')
