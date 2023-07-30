# Dockerize Service Latency Monitor

A simple service monitor that executes an HTTP call to an endpoint and logs the response time.

- Dockerfile
- Monitoring Logic
- Monitoring Configuration File
- Database Adaptor
  - DynamoDB

The program reads a list of urls from the config file, how often to perform the call and then executes the HTTP call
logging the response time, response code, timestamp of call.

The url list is refreshed at the specified interval so that URLs can be added/removed without restarting the program.

A separate service should be developed to analyze the data and perform actions (i.e. alert support, remove endpoint from 
load balancer, etc)
