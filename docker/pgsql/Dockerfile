#
# Postgresql Dockerfile
#
# Pull base image.
FROM postgres:12.6

# Environment for postgresql
ENV POSTGRES_USER="005user"
ENV POSTGRES_PASSWORD="005project"
ENV POSTGRES_DB="db"

# Install packages
RUN apt-get update && apt-get install iputils-ping nano mc curl -y

# Port 
EXPOSE 5432



