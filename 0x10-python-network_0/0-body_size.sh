#!/bin/bash
#  sends a request to that URL, and displays the size of the body of the response
curl -I $1 | grep Content-Lenght | cut -d ' ' -f2
