#!/bin/bash
# Bash script that takes in a URL, sends a request to that
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
