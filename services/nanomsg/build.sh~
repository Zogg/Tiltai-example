#!/bin/bash

git clone https://github.com/Zogg/Tiltai.git
cd Tiltai
python setup.py sdist
cp dist/ProjectX-0.1.0.tar.gz ../
sudo docker build -t zogg/nanomsg .
