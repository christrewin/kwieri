FROM ubuntu:latest
RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /data
RUN mkdir -p /logs
RUN apt-get install -y tar git curl wget dialog net-tools build-essential

RUN apt-get -y install apache2 openssl
RUN a2enmod rewrite

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

RUN apt-get install -y python python-pip python-virtualenv gunicorn

# Copy files into place.
ADD /app /app

ADD requirements.txt /data/requirements.txt
RUN pip install -r /data/requirements.txt

# Update the default apache site with the config we created.
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf

ADD supervisor.conf /etc/supervisor/conf.d/supervisor.conf
EXPOSE 80 5000
CMD ["/usr/bin/supervisord"]
