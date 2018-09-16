#!/usr/bin/env python3

from time import sleep, asctime, time
from picamera import PiCamera
import dropbox
import pathlib
import os

camera = PiCamera()
# camera.resolution = (1024, 768)
camera.resolution = camera.MAX_RESOLUTION
camera.start_preview()

sleep(2)

d = dropbox.Dropbox(os.environ['IRCAM_TOKEN'])
while True:
    fl = pathlib.Path(".")
    fn = str(int(time())) + '.png'
    ff = fl / fn
    print('capturing ' + fn + ' ...')
    camera.capture(fn)
    print('uploading ' + fn + ' ...')
    with ff.open('rb') as f:
        d.files_upload(f.read(), '/ircam/' + fn, mode=dropbox.files.WriteMode("overwrite"))
    os.remove(fn)
