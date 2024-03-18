#! /usr/bin/env python3

import os
import requests

os.chdir('/home/student-03-ef3e8b274a0f/supplier-data/descriptions')

filedir = os.listdir()
Data_Dict = {}
Txt_files = []
for items in filedir:
         if items.endswith('.txt'):  
                   Txt_files.append(items)    

for files in Txt_files:   
        with open(files, "r") as file:
            line1 = file.readline()
            line2 = file.readline()
            line2 = [int(line2.split()[0])]
            #  will remove whitespace after int 
            line3 = file.read()
            Data_Dict['name'] = line1
            Data_Dict['weight'] = line2
            Data_Dict['description'] = line3
            Data_Dict['image_name'] = files.replace("txt", "jpeg")
            response = requests.post("http://34.82.3.102/fruits/", data=Data_Dict)



            