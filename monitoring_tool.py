#!/usr/bin/env python3
from pythonping import ping
from datetime import datetime
import psutil
import sys
import json
import requests

# Slack Notification
def slackNotif(data_json):
    url = 'https://hooks.slack.com/services/*****************************'
    requests.post(url, json = data_json)

    return;

# CPU Usage
# Slack Notification on crossing threshold of 80% of CPU Usage
def cpuUsage():
    "This function prints the %ge of CPU utilization"
    cpuThreshold = 80

    c = psutil.cpu_percent(interval=1)
    print('CPU %:', c)

    if  c > cpuThreshold:
        data_json = {"text":"Warning!! CPU Usage threshold crossed"}
        slackNotif(data_json)
    return c;

# Memory Usage
# Slack Notification on crossing threshold of 80% of Memory Usage
def memoryUsage():
    "This function prints the %ge of Memory Usage"
    memoryThreshold = 80

    m = psutil.virtual_memory()[2]
    print('Memory % used:', m)

    if m > memoryThreshold:
       data_json = {"text":"Warning!! Memory Usage threshold crossed"}
       slackNotif(data_json)
    return m;

# Disk Usage
# Slack Notification on crossing threshold of 90% of Disk Usage
def diskUsage(path):
    "This function prints the %ge of Disk Usage"
    diskThreshold = 90

    d = psutil.disk_usage(path)[3]
    print('Disk % Used:', d)

    if d > diskThreshold:
       data_json = {"text":"Warning!! Disk Usage threshold crossed"}
       slackNotif(data_json)
    return d;

# Network Latency
def networkLatency(host):
    "This function will show average response time, maximum response time and minimum response time"
    x = ping(host)
    print('Minimum Response Time for',host,':', round(x.rtt_min*1000,2), 'ms')
    print('Maximum Response Time',host,':', round(x.rtt_max*1000,2), 'ms')
    print('Average Response Time',host,':', round(x.rtt_avg*1000,2), 'ms')
    return;


# Main Funtion
# Display stats in particular time
def main():
    x = sys.argv[1]
    y = sys.argv[2]

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("System Stats at", current_time," :")

    cpuUsage()
    memoryUsage()
    diskUsage( path=y)
    networkLatency( host=x)

if __name__ == "__main__":
    main()
