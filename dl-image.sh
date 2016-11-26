#!/bin/bash -e

\ssh -i ~/.ssh/id_rsa pi@192.168.0.7 "raspistill -n -o image.jpg" && scp pi@192.168.0.7:image.jpg . && open image.jpg
