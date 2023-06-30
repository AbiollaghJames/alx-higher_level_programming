#!/bin/bash
# A script that sends request to URL and displays the size of the response body
curl -sI "$1" | awk '/Content-Length/ {print $2}'
