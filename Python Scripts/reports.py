#!/usr/bin/env python3

import os
import sys
import datetime

os.chdir('/home/student-03-ef3e8b274a0f/supplier-data/descriptions')
filedir = os.listdir()
Data_Dict = {}
Txt_files = []
Formated_txt = []
for items in filedir:
         if items.endswith('.txt'):   
                   Txt_files.append(items)    
for files in Txt_files:
        with open(files, "r") as file:
              line1 = file.readline()
              line2 = file.readline()
              name = line1
              weight = line2
              Formated_txt.append(f"name: {name}<br/>")
              Formated_txt.append(f"weight: {weight}<br/>")
              Formated_txt.append("<br/>")

format_for_pdf = '\n'.join(Formated_txt)


from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("/tmp/processed.pdf")
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
styles = getSampleStyleSheet()
from datetime import datetime
time_right_now = datetime.now()            
current_date = time_right_now.strftime('%B %d, %Y')
report_title = Paragraph(f"Processed Update on {current_date}", styles["h1"])


text = Paragraph(format_for_pdf)
report.build([report_title, text])

