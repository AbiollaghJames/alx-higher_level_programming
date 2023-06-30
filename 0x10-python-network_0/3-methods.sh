#!/bin/bash
#a Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -sX OPTIONS -L "$1" | awk '/^Allow:/ {print$2}'
