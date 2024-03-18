#!/usr/bin/env python3

import requests
import os

# Upload files to website
jpeg_files = []
os.chdir('/home/student-03-ef3e8b274a0f/supplier-data/images')
filedir = os.listdir()
url = "http://localhost/upload/"
for items in filedir:
         if items.endswith('.jpeg'):   
                   jpeg_files.append(items) 

for files in jpeg_files:
    with open(files, 'rb') as file:
      r = requests.post(url, files={'file': file})