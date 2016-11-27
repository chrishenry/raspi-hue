#!/bin/bash -e

apt-get install -y build-essential cmake pkg-config

apt-get install -y libjpeg8-dev libjasper-dev libpng12-dev
# Also, libtiff4-dev. Not really using TIFF, so should be OK

# For GUIs
# apt-get install -y libgtk2.0-dev

# For Video
# apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

apt-get install -y python2.7-dev

# Upgrade pip, too
pip install -U pip
