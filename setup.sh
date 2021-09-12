#!/bin/bash
sudo apt install -y python3 python3-pip ffmpeg
pip3 install git+https://github.com/flyingrub/scdl
pip install -r requirements.txt
mkdir music
python3 run.py
