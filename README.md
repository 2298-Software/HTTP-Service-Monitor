# Dockerize Service Latency Monitor

It is important to monitor and log the uptime and latency of services.  This will allow us to see latency over time, be proactive by detecting and fixing issues before they happen, and determine if an update or new release has degraded service.

Have you ever had users report "slowness," and you can't find any issue while looking through the logs?  Maybe the version of Java was updated, and you would like to know if it impacted service response times?  Maybe a new version of your API was deployed; how do you know if it's faster/slower than the previous version?  You need a service monitor if you answered yes to any of these.  There are out-of-the-box tools and services to do this, but if you want ultimate control, then write it yourself...besides who wants to run somebody else's code when you can write your own?

This simple service monitor is written in Python and deployed as a containerized service through the AWS App Runner service.

A simple service monitor that executes an HTTP call to an endpoint and logs the response time.

- Dockerfile
- Monitoring Logic
- Monitoring Configuration File

The program reads a list of urls from the config file, how often to perform the call and then executes the HTTP call
logging the response time, response code, timestamp of call.

The url list is refreshed at the specified interval so that URLs can be added/removed without restarting the program.

A separate service should be developed to analyze the data and perform actions (i.e. alert support, remove endpoint from 
load balancer, etc)

## Code Inventory
- Dockerfile - container definition
- app.py - the logic
- urls.json - a list of URLs to monitor
- conf.json - configuration file for values like loop sleep time
- requirements.txt - a list of Python requirement

## Configuration
- batch_size - number of records to hold in memory before saving to file
- reload_seconds - the number of seconds before the url list will be refreshed from disk
- sleep_seconds - number of seconds to sleep between iterations
- output_file - the name of the output file

## Conf.json
```json
{
  "batch_size": 100,
  "reload_seconds": 2400,
  "sleep_seconds": 10
}
```

## urls.json
```json
[
  {"url": "https://google.com"},
  {"url": "https://foxnews.com"},
  {"url": "https://cnn.com"}
]
```

## Quick Start

```shell
https://github.com/2298-Software/HTTP-Service-Monitor.git
cd service-monitor
docker build -t service-monitor:latest .
docker container run --name service-monitor -d service-monitor:latest
```