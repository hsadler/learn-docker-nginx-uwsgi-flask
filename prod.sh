
docker build -t flask-server . && \
docker run -p 4000:80 flask-server:dev
