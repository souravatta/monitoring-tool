#!/usr/bin/env python3
from pythonping import ping
from datetime import datetime
import psutil
import sys
import json
import requests


def slackNotif(data_json):
    url = 'https://hooks.slack.com/services/******************************'
    requests.post(url, json = data_json)

    return; 

def cpuUsage():
    "This function prints the %ge of CPU utilization"
    cpuThreshold = 0.0

    c = psutil.cpu_percent(interval=1)
    print('CPU %:', c)

    if  c > cpuThreshold:
        data_json = {"text":"Warning!! CPU Usage threshold crossed"}
        slackNotif(data_json)
    return c;

def memoryUsage():
    "This function prints the %ge of Memory Usage"
    memoryThreshold = 20

    m = psutil.virtual_memory()[2]
    print('Memory % used:', m)

    if m > memoryThreshold:
       data_json = {"text":"Warning!! Memory Usage threshold crossed"}
       slackNotif(data_json)
    return m;

def diskUsage(path):
    "This function prints the %ge of Disk Usage"
    diskThreshold = 0.0

    d = psutil.disk_usage(path)[3]
    print('Disk % Used:', d)

    if d > diskThreshold:
       data_json = {"text":"Warning!! Disk Usage threshold crossed"}
       slackNotif(data_json)
    return d;

def networkLatency(host):
    "This function will show average response time, maximum response time and minimum response time"
    x = ping(host)
    print('Minimum Response Time for',host,':', round(x.rtt_min*1000,2), 'ms')
    print('Maximum Response Time',host,':', round(x.rtt_max*1000,2), 'ms')
    print('Average Response Time',host,':', round(x.rtt_avg*1000,2), 'ms')
    return;


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
