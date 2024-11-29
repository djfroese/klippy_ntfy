#!/bin/bash

cd ~/klippy_ntfy
git pull origin main
sudo service klipper stop
rm ~/klipper/klippy/extras/ntfy.py
ln -s ~/klippy_ntfy/ntfy.py ~/klipper/klippy/extras/ntfy.py
sudo service klipper start

