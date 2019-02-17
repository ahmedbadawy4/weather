#!/usr/bin/env bash
pwd
sudo apt-get update
echo "install python"
sudo apt-get -y install python
sudo apt-get -y install python3-pip
pip3 install -U pip
cd /home/vagrant/weather/
sudo pip3 install -r ./requirements.txt
python3 ./app.py > /dev/null 2>&1 &
