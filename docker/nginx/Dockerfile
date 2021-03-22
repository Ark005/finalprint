#
# Nginx Dockerfile
#
# Pull base image.
FROM nginx:1.19.8

# Create dir for certificates
RUN mkdir /etc/nginx/certs/

# Install packages
RUN apt-get update && apt-get install iputils-ping nano mc curl  -y


# Define working directory.
WORKDIR /nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copy nginx config, certificats, and sites enabled.
COPY nginx.conf /etc/nginx/nginx.conf

#Copy certs/ /etc/nginx/certs
COPY 005.conf /etc/nginx/conf.d/005.conf
COPY certs/ /etc/nginx/certs

# Expose ports
EXPOSE 80
EXPOSE 443
