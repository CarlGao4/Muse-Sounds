# This file is used to generate a table of released instruments with GitHub Actions
# This should be run with GitHub Actions

import os
import requests
import re

repo = os.environ["GITHUB_REPOSITORY"]
api_url = f"https://api.github.com/repos/{repo}/releases?per_page=100&page="
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {os.OUTPUTiron['GITHUB_TOKEN']}",
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

instruments = {}
instrument_urls = {}
for release in releases:
    catagory, name = release["name"].split(" - ", 1)
    if catagory not in instruments:
        instruments[catagory] = {}
        instrument_urls[catagory] = {}
    assert name not in instruments[catagory], f"Duplicate instrument name {name} in catagory {catagory}"
    instruments[catagory][name] = {}
    instrument_urls[catagory][name] = release["html_url"]
    for asset in release["assets"]:
        instruments[catagory][name][asset["name"]] = asset["browser_download_url"]

try:
    with open("instrument.md", mode="rt", encoding="utf-8") as f:
        old_markdown = f.read()
except FileNotFoundError:
    old_markdown = ""

markdown = "# Instruments\n\n"

for catagory in sorted(instruments.keys()):
    markdown += f"## {catagory}\n\n"
    for name in sorted(instruments[catagory].keys()):
        markdown += f"- [{name}]({instrument_urls[catagory][name]})\n"
        for asset in sorted(instruments[catagory][name].keys()):
            markdown += f"  - [{asset}]({instruments[catagory][name][asset]})\n"
    markdown += "\n"

print("Generated markdown:")
print(markdown)

# Only write the file if the contents have changed
if markdown != old_markdown:
    os.system('echo "continue_commit=true" >> "$GITHUB_OUTPUT"')
    with open("instrument.md", mode="wt", encoding="utf-8") as f:
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
