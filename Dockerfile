FROM alpine
# Linux packages
RUN apk update
RUN apk add --no-cache python3 py3-pip cloc

# Python packages
COPY requirments.txt /app/requirments.txt
RUN pip3 install -r /app/requirments.txt

COPY . /app/

ENV GUNICORN_WORKERS 1
ENV GUNICORN_THREADS 2

# gunicorn args:
# -w               | Number of workers
# -t               | Number of threads
# --worker-class   | Type of workers
# --worker-tmp-dir | gunicorn uses heatbeat files for workers. /dev/shm is in
#                    memory so it's more effecient. Dockers /tmp is not in
#                    memory which causes hangs
# -b               | bind to a ip/port
# --chdir          | changes to the source directory
# - c              | custom config file
ENTRYPOINT gunicorn -w=$GUNICORN_WORKERS -t=$GUNICORN_THREADS --worker-class=gthread \
	--chdir /app/ \
	--worker-tmp-dir /dev/shm \
	# --certfile=./certs/server.crt \
       	# --keyfile=./certs/server.key \
	-c /app/config.py \
	-b 0.0.0.0:80 \
	main:app

# Run the app - mount the code for easier development
# docker run -p 444:444 -v ~/projects/api/:/mnt/app: flask
