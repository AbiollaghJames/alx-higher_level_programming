#!/bin/bash
# Bash script that takes in a URL, sends a request to thait
curl -sI "$1" | awk '/Content-Length/ {print $2}'
