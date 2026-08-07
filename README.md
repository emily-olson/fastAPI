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
Didn't actually do anything with Redis here, but I wanted to understand what Redis is and where it's actually used. Redis is an in-memory key-value store that supports rich data types (lists, hashes, vectors, etc), low-latency (since accessing from RAM is faster than from disk), and persistence (sort of, it periodically writes to disk and/or keeps a log of writes). It is different than like a disk-based DB's buffer cache that lives in RAM (for example, PostgresSQL has an in-memory buffer
cache) in that it doesn't just store like SQL type pages from the disk, which is what PostgresSQL cache is. Rather, it actually stores like application objects that you can define and write/read from Redis. So instead of storing like a page from disk with tables of customer names, you could actually store things like name, time of log in, API calls made in this session, etc (this is like user session data, something Redis is popular for). Redis has been optimized to store all sorts of
fancy things and compute fancy operations quickly like sorted sets, expirations (TTLs), etc. 

A couple examples of where Redis is used:
Github: uses it to store user session data
Twitter: rate limiting (you can only make 100 requests per minute, Redis stores how many requests a user has made and sends errors when they go over)

Also, an interesting use case now with AI is that Redis can cache prompt hashes/semantics so that when similar questions are asked by different users, the response can be served from the cache. It can also store like vector embeddings and search results, for fasted vectorized semantic search (you can store vector sets in Redis, don't need a special vector DB). 

That being said, some people say that Redis is kinda unnecessary and that its not really that much faster than just using a disk database itself. 
