#!/bin/bash
LOG_FILE="var/log/myapp/system_metrics.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

echo "$TIMESTAMP | cpu=$(cat /proc/loadavg) | mem=$(free -m | awk '/Mem:/ {print $7} ') | disk=$(df -h | awk '$6=="/" {print $5}')" >> "$LOG_FILE"