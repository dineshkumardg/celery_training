FROM python:3.6
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get install -y apt-utils && rm -rf /var/lib/apt/lists/*

RUN echo "Europe/Madrid" > /etc/timezone; dpkg-reconfigure --frontend noninteractive tzdata

WORKDIR /app
COPY celery_prj/ /app
RUN pip install -r /app/requirements.txt --no-cache-dir


# COPY startup script into known file location in container
#COPY start.sh /start.sh

# EXPOSE port 8000 to allow communication to/from server
#EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
#CMD ["/start.sh"]
# done!
