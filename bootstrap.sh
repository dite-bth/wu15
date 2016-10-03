#!/usr/bin/env bash

# Use single quotes instead of double quotes to make it work with special-character passwords
PASSWORD='password'

# update / upgrade
sudo apt-get update
#sudo apt-get -y upgrade

# install python
sudo apt-get install python2.7

# install mysql and give password to installer
sudo debconf-set-selections <<< "mysql-server mysql-server/root_password password $PASSWORD"
sudo debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $PASSWORD"
sudo apt-get -y install mysql-server

# install MySQLdb for python
sudo apt-get -y install python-mysqldb

# install git
sudo apt-get -y install git
