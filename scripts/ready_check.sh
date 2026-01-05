#!/bin/bash
URL="http://localhost:8081/ready"

echo "---------------Readiness check----------------------"

status_code=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 --max-time 10 "$URL")

if [ "$status_code" -eq "200" ]; then 
    echo "status:ready"
    exit 0
else
    echo "status:Not ready"
    exit 1
fi