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

Also, DynamoDB is an AWS service, didn't know that. 

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
