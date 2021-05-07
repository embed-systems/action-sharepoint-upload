# Container image that runs your code
FROM python:3.9.5-slim

# RUN apk add gcc --update   # cairo-dev pango-dev gdk-pixbuf-dev
RUN pip install Office365-REST-Python-Client

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /app/entrypoint.sh
COPY main.py /app/main.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/app/entrypoint.sh"]
