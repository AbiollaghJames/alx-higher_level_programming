#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL "$1" -w "%{http_code}" -o {print $2}
