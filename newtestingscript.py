import imp
import requests

#webscrapping
from bs4 import BeautifulSoup
#send mail
import smtplib
#emailbody
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#sytemdate and time manipulation
import datetime

now = datetime.datetime.now()

#emal content placeholder

content = ''
