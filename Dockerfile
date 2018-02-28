
# parent image
FROM ubuntu:16.04

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the container at /app
ADD . /app

# OS installs
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
    git \
    python-pip \
    python-dev \
    nginx

# install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# make port 80 available to the world outside this container
EXPOSE 80

# run app.py when the container launches
CMD ["python", "app.py"]
