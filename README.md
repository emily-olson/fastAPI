# FastAPI
## This is my tiny fastAPI server project, so I can learn more about APIs, HTTP, etc.

## Setup Instructions
To get started, follow this setup:
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Run Instructions
Then, to run, do the following:
```bash
uvicorn main:app --reload
```
And visit http://localhost/docs to see the available endpoints.

Or, you can run it via Docker.
```bash 
docker compose up --build
```

## AWS EC2
As a learning exercise, I also deployed my tiny fastAPI to EC2. It was a good learning experience in that I was able to explore the AWS Dashboard, launch and connect to an instance (via the browser), and see my app running on the "rented" AWS IP address. 

EC2 is the Elastic Compute Cloud. AWS loans you a server (so they manage the hardware) but you manage all the software: the OS, the networking, the actually software you want to run, etc. You can get like pre-built and confiugured EC2 instances if your app has like settings that are common, but you can also configure it yourself. You pay for the server all the time, even if your app is not actively getting traffic. 

Also, DynamoDB is an AWS service, didn't know that. 

## AWS S3
The AWS Simple Storage Service. Built for scalability, security, etc. It is now marketing itself as a good storage service for AI training (put all your training data here!). It can store all sorts of data from vectors, to unstructured, to structured data. Comes with data pipelines to feed it back to you. 

## AWS Lambda
Similar to EC2 except AWS loans you like anonymous servers that you don't get to configure yourself, you just tell Lambda what software you want to run and when ("event sources": what events do you want to trigger this code to run). AWS will only charge you when the software runs, so it can be cheaper. Except you get less customization: you are not responsible for the config of the server. 

## Redis
Didn't actually do anything with Redis here, but I wanted to understand what Redis is and where it's actually used. Redis is an in-memory key-value store that supports rich data types (lists, hashes, vectors, etc), low-latency (since accessing from RAM is faster than from disk), and persistence (sort of, it periodically writes to disk and/or keeps a log of writes). It is different than like a disk-based DB's buffer cache that lives in RAM (for example, PostgresSQL has an in-memory buffer cache) in that it doesn't just store like SQL type pages from the disk, which is what PostgresSQL cache is. Rather, it actually stores like application objects that you can define and write/read from Redis. So instead of storing like a page from disk with tables of customer names, you could actually store things like name, time of log in, API calls made in this session, etc (this is like user session data, something Redis is popular for). Redis has been optimized to store all sorts of fancy things and compute fancy operations quickly like sorted sets, expirations (TTLs), etc. 

A couple examples of where Redis is used:
Github: uses it to store user session data
Twitter: rate limiting (you can only make 100 requests per minute, Redis stores how many requests a user has made and sends errors when they go over)

Also, an interesting use case now with AI is that Redis can cache prompt hashes/semantics so that when similar questions are asked by different users, the response can be served from the cache. It can also store like vector embeddings and search results, for fasted vectorized semantic search (you can store vector sets in Redis, don't need a special vector DB). 

That being said, some people say that Redis is kinda unnecessary and that its not really that much faster than just using a disk database itself. 

## Kafka
Also didn't use Kafka here. But, Kafka is open source software under Apache that serves a messaging stream for producers and consumers. It is an append only log, so messages keep getting added and you can not delete/edit old ones. So in some large architecture you probably have producers (services publishing data) and consumers (services consuming data). But, you don't want interservice communication to be tightly coupled, meaning those two services talk directly to each other (that is messy for scalability, updating architecture, building custom pipelines, etc). Instead, it would be great if there was some place to put data and read data for all producers and consumers. Kafka! It is a river of data, separated into streams (topics), further separated into partitions (basically divide data up into partitions so many consumers can read same topic at a time and not all be reading from exact same stream). Kafka does NOT tell a service to produce data (like it doesn't call an API or anything) but it can accept produced data into the river, and then have it accessible to any consumser who wants it (for example, many services may want to read the same data -- like a data analytics service, a performance service, etc). Unlike message queues, the messages do not get deleted/disappear after someone reads them. Instead, they are accessible to many consumers and also the data gets permanently stored in the Kafka database (lives on disk, is basically a log file), so someone can read the data today and another person can read it in three days. Also, it can handle tons of data in the river, good for having like millions of transactions or something. 

A "broker" if you ever see that is just a Kafka server (so a machine that runs Kafka software and stores its data) that handles the work of putting messages in a topic, partitioning it, etc. You can have a cluster of brokers so that you can horizontally scale your Kafka for more storage, more throughout, better fault tolerance (you can replicate data across diff brokers). The producer does not decide what broker to use, instead Kafka main server (?) decides what broker this data should go to based on like key hashing or round robin) and also the main server directs a consumer to the right broker when it wants to read data. 

Recently, it's been popular for ML training and Kafka has even said that it can serve ML training without requiring any external storage service like S3, all the data just gets streamed through Kafka that you could need. Idk much about this though. 

## Kubernetes
I am so tired. Anyways, I should practice deploying something with Kubernetes instead of just reading about it, but I don't have time or the energy. 

What I've learned is that Kubernetes essentially orchestrates running multiple containers (containers being like packaged software) together at once. You could be running many servers with the same container if the container software is heavily used, or you could also be using Kubernetes to run many different types of containers together (ie they work together in some way). It basically handles spinning up all the containers (so you don't have to run docker compose/run for everything single one), starting a new container when one fails, managing what machines are free and can run your container, performing load balances, making little software updates if needed to get containers to run together without crashing/stopping the whole system to make the change, figuring out how to get containers to talk to each other (and which ones are allowed to talk to who).

Also, its not like people necessarily just run Kubernetes on its own. They often use some other service that includes Kubernetes in it, such as AWS EKS. Kubernetes doesn't come built in with networking or security for example. It is just an "OS" that manages different containers ("OS" in quotes because it is similar to how an OS manages different processes, also heard someone say it is like an "OS" for the cloud). Kubernetes allows many computers (nodes) to work together as one. 

That's why the kubernetes logo is the ship steering wheel thing: it manages and runs a whole bunch of containers.
Kubernetes figures out what machines to use in an optimal way (take advantage of CPU without killing it). For updates, new images can be pulled and deployed as containers seamlessly. 

There are some key terms you need to know:

Container: code, config, dependencies of a program such that it can run as an isolated process on any system
** kubernetes supports many container running engines, including Docker (which is the most popular but not the only one)
Pod: holds a container (usually one, but sometimes two if the two containers are tightly coupled -- talk directly to each other). is a single instance of an application
Node: groups of pods are held on a single machine (virtual or physical)
Cluster: groups of nodes (ie machines)

How to actually use it: they have an API (REST) that is often called kubectl (command line interface). People call this like "cube cuttle". Then there are like "operators" that manage the control plane which is what is actually telling the servers what to do. But that's kinda out of scope for not. 

Note that Kubernetes by itself is not really enough. Many organizations also want logging, metrics, automation, CI/CD, etc. So, there are many tools that use Kubernetes as its foundation but then also include all these other services. One example is RedHat OpenShift.

People usually call Kubernetes K8s. K3s is just a lightweight version of Kubernetes that is easier to install and is meant for like smaller production environments. You may only need K8s for large production environments. But it is the same concept and you use the same API and behavior. 

## CI/CD
This is like pretty obvious but its essentially the idea of continuous integration & continous deployment. So, instead of have many branches of source code merged on like one "merge day" with risks of lots of errors, and also crashing the whole system, changes should be continuously integrated into the application and deployed to users. In order to achieve this, there are DevOps people who are in charge of facilitating the pipeline of developer pushed changes to deployment. This involves tons of automated testing, end to end tests, etc. Essentially, since everyone is making changes that may not only affect the app but also may conflict with someone else's active changes, it is better to continuously integrate and test them so everyone is on the same page. 
