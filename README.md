# Report-Automation-Py-Project
Automating website and system tasks with python!

Using various Python scripts to automate the tasks of importing data and updating a website as well as using system checks to check cpu usage and various other metrics that will send an email warning if metric at crtical levels.

changeImage.py will convert all images in a specificed directory to jpeg format

supplier_image_upload.py will upload the jpeg images in a specified directory to the website for use with data supplied.

Run.py will iterate through txt files and upload the txt with the corresponding image on the website referecned and using requests will update the website with the data providing automation for website updates.

Reports.py will take the data in the txtfiles and generate it into a pdf report.

report_email.py will take the pdf report and send it to the email address of localhost of the site.

health_check.py will monitor system stats and report an error if cpu usage is over 80%, avaiable memory is under 500mb, there is less than 20% disk space or if hostname cannot be resolved.