
# parent image
FROM ubuntu:16.04

# OS installs
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
    wget \
    grep \
    git \
    curl \
    python-pip \
    python-dev \
    nginx \
    tree
