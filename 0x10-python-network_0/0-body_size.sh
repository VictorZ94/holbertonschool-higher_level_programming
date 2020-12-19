#!/bin/bash
#  sends a request to that URL, and displays the size of the body of the response
# I'm using --silent to avoid to display the content below --silent is equal to -s
#=================================================================================
# % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
#                                 Dload  Upload   Total   Spent    Left  Speed
#   0    17    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
#====================================================================================
# I'm using --head to display only header --header is equal to -I
curl --silent --head $1 | grep Content-Length | cut -d ' ' -f2
