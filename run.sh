#!/bin/bash
while true
do
    echo "$(date) - my app is running" >> /var/log/myapp/app.log
    sleep 5 
done