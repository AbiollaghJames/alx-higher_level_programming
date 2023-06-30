#!/bin/bash
# Bash script that takes in a URL, sends a request to thait
url=$1
size=$(curl -s -w '%{size_download}' -o /dev/null "$url")
echo "$size"
