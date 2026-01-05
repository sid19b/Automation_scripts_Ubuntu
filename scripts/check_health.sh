#!/bin/bash
URL="http://localhost:8081/health"

echo "---------------Health check----------------------"

status_code=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 --max-time 10 "$URL")

if [ "$status_code" -eq "200" ]; then 
    echo "status:ok"
    exit 0
else
    echo "status:Not ok"
    exit 1
fi