#!/bin/bash

set -e

### install docker and other packages on main vps(digital ocean)
yum update
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install python3 python3-pip yum-utils docker-ce docker-ce-cli containerd.io curl nano mc git lvm2 -y
curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
systemctl start docker
mkdir /005
mkdir /data
mkdir /data/project
mkdir /data/bd
cp /005 /data/project
cd /005/docker && docker-compose up -d --build



