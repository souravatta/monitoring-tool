Monitoring Tool
=========================

This monitoring tool is used to monitor the status of the machine on following criteria:

* CPU Usage
* Memory Usage
* Disk Usage
* Network Latency

---

Requirements
------------
1) User should have sudo access to run the python file.
2) Use python3
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

Example 1 cpuUsage()
------------------

```python

def cpuUsage():
    "This function prints the %ge of CPU utilization"
    cpuThreshold = 0.0

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
