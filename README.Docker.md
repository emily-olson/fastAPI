### Building and running your application

When you're ready, start your application by running:
`docker compose up --build`.

Your application will be available at http://localhost:8000.

Emily's notes: `compose` basically encapsulates `docker build`, `docker run` (so it takes the dockerfile, makes an image, creates a container, and runs the container). The steps it takes are outlined in the compose.yml file (instructions for the compose step!!!). It's a faster command, since you don't have to type all the individual commands. It gives the image a random name (not random, but like fastapi:latest or something). So, when you want to push to Docker Hub you often have to rename the image so it makes sense to other people. 

### Deploying your application to the cloud (ie put it on DockerHub)

First, build your image, e.g.: `docker build -t fastapi-app .`. (NOTE: you can call it whatever you want, fastapi-app, fastapi-main, fastapi-test. when you run docker image ls, you will just see all of these images with diff names!) Also, the `.` just saying use the current directory to find the Dockerfile. The `-t` means add a tag. You can specify one manually like fastapi-app:latest or fastapi-app:v1, but if you do not, then Docker will choose one by default. 

Now you have an image. If you wanted to run it, you can do `docker run fastapi-app` or `docker run fastapi-app:latest`. 

If you want to give your image another name (eg for pushing it to Docker hub with a clearer name), you can just do `docker tag fastapi-app:latest olsonemily/fastapi-app:newtagname`. All this does is give the SAME image another tag name. 

Finally, you can push: `docker push olsonemily24/fastapi-app:latest`. 

If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)
