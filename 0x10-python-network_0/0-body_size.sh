#!/usr/bin/bash
# Bash script that takes in a URL, sends a request to that
#URL, and displays the size of the body of the response

#url from 1st arg
url=$1

#send request and get size
size=$(curl -s -w '%{size_download}\n' -o /dev/null "http://$url")

#Display size
echo "$size"
