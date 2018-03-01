
# parent image
FROM ubuntu-base

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the container at /app
ADD . /app

# install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# make port 80 available to the world outside this container
EXPOSE 80

# run app.py when the container launches
CMD ["python", "app.py"]
