#!/bin/bash
# 
curl -o /dev/null -w '%{http_code}' -sLI "$1"
