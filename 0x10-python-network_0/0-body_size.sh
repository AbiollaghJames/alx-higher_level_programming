#!/bin/bash
# Bash script that takes in a URL, sends a request to thait
size=$(curl -s -w '%{size_download}' -o /dev/null "$$1") | echo "$size"
