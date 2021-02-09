Monitoring Tool
=========================

This monitoring tool is used to monitor the status of the machine on following criteria:

* CPU Usage
* Memory Usage
* Disk Usage
* Network Latency

It will send slack notification to a channel, when:

* CPU Usage is above 80%
* Memory Usage is above 80%
* Disk Usage is above 80%

---

Requirements
------------
1) User should have sudo access to run the python file.
2) Use python => 3.6.0
---

Functions Used
--------------

* **slackNotif(data_json)** : Used to send the slack notification (Warning on Usage) to particular channel.
* **cpuUsage()** : Used to monitor the CPU usage
* **memoryUsage()** : Used to monitor the memory usage
* **diskUsage(path)** : Used to monitor the disk usage
* **networkLatency(host)**: Used to monitor the network latency (min/max/avg response time) of particular host. Ex. google.com etc.
* **main()**: Call the all other functions to print the System Stat at that specific time
---

Example 1 slackNotif(data_json)
-----------------------------

```python

def slackNotif(data_json):
    url = 'https://hooks.slack.com/services/******************************'
    requests.post(url, json = data_json)

    return;

```
---

Example 2 cpuUsage()
------------------

```python

def cpuUsage():
    "This function prints the %ge of CPU utilization"
    cpuThreshold = 80

    c = psutil.cpu_percent(interval=1)
    print('CPU %:', c)

    if  c > cpuThreshold:
        data_json = {"text":"Warning!! CPU Usage threshold crossed"}
        slackNotif(data_json)
    return c;

```
---

Usage
-----
1) After you clone this repo to your desktop, run the **monitoring_tool.py** with the sudo user.
2) It will take into two  arguments:
	1) host (to monitor the network latency): Ex. google.com
	2) path of mount point or disk: Ex. /
3) Install the dependiencies: `pip install requirements.txt`
4) Command to run: `sudo python3 monitoring_tool.py google.com /`
---

Setting up Slack Notification
----------------------------

1) Create a Custom App say monitBot.
2) Select the Development Slack Workspace and click on `Create App`
3) Under `Features` >> `Incoming Webhooks`, Activate incoming webhooks
4) Click on `Add New Webhook to Workspace` >> Select the channel >> Click on Allow
5) Copy the Webhook Url and paste it in the `python file` inside the function `slackNotif(data_json)`

![Slack Notification](https://github.com/souravatta/monitoring-tool/blob/main/slack_notification.png?raw=true)
