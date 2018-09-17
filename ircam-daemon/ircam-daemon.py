#!/usr/bin/env python3

from time import sleep, asctime, time
from picamera import PiCamera
import dropbox
import pathlib
import os

access_token = os.environ.get('IRCAM_TOKEN')
if access_token == None:
    print('IRCAM_TOKEN is not presented.')
    print('usage: IRCAM_TOKEN="<access_token>" ./ircam-daemon.py')
    exit(0)

print('PiCamera initialization...')
camera = PiCamera()
camera.resolution = camera.MAX_RESOLUTION
camera.start_preview()
sleep(2)
print('PiCamera is ready!')

d = dropbox.Dropbox(os.environ['IRCAM_TOKEN'])
while True:
    fl = pathlib.Path(".")
    fn = str(int(time())) + '.png'
    ff = fl / fn
    print('Capturing "' + fn + '"...')
    camera.capture(fn)
    print('Uploading "' + fn + '"...')
    with ff.open('rb') as f:
        d.files_upload(f.read(), '/ircam/' + fn, mode=dropbox.files.WriteMode("overwrite"))
    print('Removing "' + fn + '"...')
    os.remove(fn)
