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
uvicorn main:app -reload
```
And visit http://localhost/docs to see the available endpoints.

Or, you can run it via Docker.
```bash 
docker compose up --build
```
