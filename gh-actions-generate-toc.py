# This file is used to generate a table of released instruments with GitHub Actions
# This should be run with GitHub Actions

import boto3
import datetime
import json
import os
import re
import requests
import sys
import urllib.parse


instruments = {}

try:
    with open("all-downloads.md", mode="rt", encoding="utf-8") as f:
        old_markdown = f.read()
except FileNotFoundError:
    old_markdown = ""


# Retrieve file list from S3

download_url_prefix = os.environ["DOWNLOAD_URL_PREFIX"]
endpoint_url = os.environ["ENDPOINT_URL"]
access_key = os.environ["ACCESS_KEY"]
secret_key = os.environ["SECRET_KEY"]
bucket_name = os.environ["BUCKET_NAME"]

release_files = {}
descriptions = {}
descriptions_pending = {}

s3 = boto3.client(
    "s3", endpoint_url=endpoint_url, aws_access_key_id=access_key, aws_secret_access_key=secret_key, verify=True
)

objects = s3.list_objects_v2(Bucket=bucket_name, MaxKeys=1000000, Prefix="public/")["Contents"]
for i in objects:
    parts = i["Key"].split("/")[1:]
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
    filename = re.sub(r"[\[\]_]", lambda m: f"\\{m[0]}", i["Key"].rsplit("/", 1)[1].replace("\\", "\\\\"))
    if "release" in parts[0]:
        if catagory not in release_files:
            release_files[catagory] = {}
        if name not in release_files[catagory]:
            release_files[catagory][name] = []
        release_files[catagory][name].append(filename)
    descriptions_pending[json.loads(i["ETag"])] = (catagory, name, filename)
    instruments[catagory][name][filename] = (
        urllib.parse.urljoin(download_url_prefix, urllib.parse.quote(i["Key"])),  # type: str
        i["Size"],  # type: int
        i["LastModified"].astimezone(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M (UTC)")
    )

r = requests.post("https://dl.muse-sounds.work/get-descriptions", json={"etags": list(descriptions_pending.keys())})
if r.status_code == 200:
    for etag, description in r.json().items():
        if description is not None:
            descriptions[descriptions_pending[etag]] = description


# Generate markdown


def human_readable_size(size):
    for unit in ["B", "KiB", "MiB", "GiB", "TiB", "PiB"]:
        if size < 20480:
            return f"{size:.5g} {unit}"
        size /= 1024


markdown_insts = "# Instrument List\n\n"

markdown_insts += (
    "If the previews can't be displayed on GitHub, please [click here](https://about.muse-sounds.work/instruments).\n\n"
    "We constantly update converted releases and add new instruments for better effects. If a download link is "
    "unavailable, please wait a moment and try again. We will not notify you of updates, so you could check last "
    "updated time from time to time and download the latest version.\n\n"
    "For Chinese users: CloudFlare only has CDN nodes in Mainland China for business users. If your download speed "
    "is slow, you can manually change the domain name in the download link from `dl.muse-sounds.work` to "
    "`dl-cn.muse-sounds.work`, which may uses better CDN nodes and routing. However, I don't guarantee it's faster.\n\n"
    "## About File Types\n\n"
    "- `*.sf2`: Converted SF2 format soundfont file.\n"
    "- `*.sf3`: Converted SF3 format soundfont file.\n"
    "- `*.sfz+flac.zip`: Converted SFZ files with FLAC audio files. You can use it directly in SFZ player.\n\n"
)

markdown_insts += (
    "## Converted Releases\n\n"
    "These are the instruments that have been converted to standard formats so you can use them in your favorite "
    "software. There is no need to download extra files, just extract it (if it is archived) and load it. "
    "I've checked the SFZ, SF2, and SF3 files in MuseScore 3.6.2 and they work well.\n\n"
)
for catagory in sorted(release_files.keys()):
    markdown_insts += f"### {catagory}\n\n"
    for name in sorted(release_files[catagory].keys()):
        markdown_insts += f"#### {name}\n"
        for asset in sorted(release_files[catagory][name], key=lambda x: tuple(reversed(re.match(r"(.*?(\.[^ ]+))", x).groups()))):
            asset_name = asset.replace("\\_", "_").replace("\\[", "[").replace("\\]", "]").replace("\\\\", "\\")
            markdown_insts += f"<details><summary>{asset_name}</summary>\n\n"
            if (catagory, name, asset) in descriptions:
                markdown_insts += "> " + "\n> ".join(descriptions[(catagory, name, asset)].splitlines()) + "\n\n"
            markdown_insts += f"> Last updated: {instruments[catagory][name][asset][2]}\n> \n"
            markdown_insts += f"> [Download {asset}]({instruments[catagory][name][asset][0]}) "
            markdown_insts += f"({human_readable_size(instruments[catagory][name][asset][1])})\n\n---\n\n</details>\n\n"

markdown_insts += (
    "## All Files\n\n"
    "These are all the files available for download. They may be the original files, which may be non-standard formats "
    "or have extra files that are not needed for most users. If you are not sure what to download, you should check the "
    "converted releases above.\n\n"
    "If you are sure you need the original files, you can download them at [all downloads](all-downloads.md).\n\n"
)

markdown_full = "# All Downloads\n\n"

markdown_full += (
    "All files uploaded to the server are listed here. If you don't know what to download, you should check the "
    "[converted releases](instruments.md) first.\n\n"
    "These files may be the original files, which may be non-standard formats or have extra files that are not needed "
    "for most users.\n\n"
    "We constantly update converted releases and add new instruments for better effects. If a download link is "
    "unavailable, please wait a moment and try again. We will not notify you of updates, so you could check last "
    "updated time from time to time and download the latest version.\n\n"
    "For Chinese users: CloudFlare only has CDN nodes in Mainland China for business users. If your download speed "
    "is slow, you can manually change the domain name in the download link from `dl.muse-sounds.work` to "
    "`dl-cn.muse-sounds.work`, which may uses better CDN nodes and routing. However, I don't guarantee it's faster.\n\n"
    "## About File Types\n\n"
    "- `*.sts.7z`: Compressed original sample files extracted from the sts file. Audio files are in opus format.\n"
    "- `*.sf2`: Converted SF2 format soundfont file.\n"
    "- `*.sf3`: Converted SF3 format soundfont file.\n"
    "- `*.sfz.7z`: Compressed original SFZ files. May not standard SFZ format and can't be loaded by SFZ player.\n"
    "- `*.sfz+flac.zip`: Converted SFZ files with FLAC audio files. You can use it directly in SFZ player.\n\n"
)

markdown_full += "## Download Links\n\n"

for catagory in sorted(instruments.keys()):
    markdown_full += f"### {catagory}\n\n"
    for name in sorted(instruments[catagory].keys()):
        markdown_full += f"#### {name}\n"
        for asset in sorted(instruments[catagory][name].keys(), key=lambda x: tuple(reversed(re.match(r"(.*?(\.[^ ]+))", x).groups()))):
            asset_name = asset.replace("\\_", "_").replace("\\[", "[").replace("\\]", "]").replace("\\\\", "\\")
            markdown_full += f"<details><summary>{asset_name}</summary>\n\n"
            if (catagory, name, asset) in descriptions:
                markdown_full += "> " + "\n> ".join(descriptions[(catagory, name, asset)].splitlines()) + "\n\n"
            markdown_full += f"> Last updated: {instruments[catagory][name][asset][2]}\n> \n"
            markdown_full += f"> [Download {asset}]({instruments[catagory][name][asset][0]}) "
            markdown_full += f"({human_readable_size(instruments[catagory][name][asset][1])})\n\n---\n\n</details>\n\n"
    markdown_full += "\n"

print("Generated instruments markdown:", file=sys.stderr)
print(markdown_insts)

print("Generated full markdown:", file=sys.stderr)
print(markdown_full)

# Only write the file if the contents have changed
if markdown_full != old_markdown:
    os.system('echo "continue_commit=true" >> "$GITHUB_OUTPUT"')
    with open("instruments.md", mode="wt", encoding="utf-8") as f:
        f.write(markdown_insts)
    with open("all-downloads.md", mode="wt", encoding="utf-8") as f:
        f.write(markdown_full)
    # Find out what instrument changed to set commit message
    old_markdown_insts = (
        dict(i[:2] for i in re.findall(r"(?<=\n)- \[?([^\[\]`\r\n]+)\]?.*\r?\n((  - .*\r?\n?)*)", old_markdown)) or
        dict((i[0], i[1]) for i in re.findall(r"#### \[?([^\[\]`\r\n]+)\]?.*\r?\n((<details><summary>.*</summary>[\s\S]+?</details>(\r?\n)*)*)", old_markdown))
    )
    new_markdown_insts = (
        dict(i[:2] for i in re.findall(r"(?<=\n)- \[?([^\[\]`\r\n]+)\]?.*\r?\n((  - .*\r?\n?)*)", markdown_full)) or
        dict((i[0], i[1]) for i in re.findall(r"#### \[?([^\[\]`\r\n]+)\]?.*\r?\n((<details><summary>.*</summary>[\s\S]+?</details>(\r?\n)*)*)", markdown_full))
    )
    added = set(new_markdown_insts.keys()) - set(old_markdown_insts.keys())
    removed = set(old_markdown_insts.keys()) - set(new_markdown_insts.keys())
    modified = {}
    for i in set(new_markdown_insts.keys()) & set(old_markdown_insts.keys()):
        links_old = (
            dict(map(reversed, re.findall(r"<summary>(.*?)</summary>[\s\S]+?\]\((.*?)\) \(.*?\)\r?\n\r?\n---", old_markdown_insts[i]))) or
            dict(map(reversed, re.findall(r"\[(.*?)\]\((.*?)\)", old_markdown_insts[i])))
        )
        links_new = (
            dict(map(reversed, re.findall(r"<summary>(.*?)</summary>[\s\S]+?\]\((.*?)\) \(.*?\)\r?\n\r?\n---", new_markdown_insts[i]))) or
            dict(map(reversed, re.findall(r"\[(.*?)\]\((.*?)\)", new_markdown_insts[i])))
        )
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
                    if modified[i][0][j].replace("\_", "_").replace("\\\\", "\\") != modified[i][1][j].replace("\_", "_").replace("\\\\", "\\"):
                        message += f"    Renamed: '{modified[i][0][j]}' -> '{modified[i][1][j]}'\n"
    message = message.replace("\_", "_").replace("\\\\", "\\")
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
