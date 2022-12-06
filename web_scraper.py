# Description:
# Web scraper and email sender with found stuff 

import requests                  # HTTP request
from bs4 import BeautifulSoup    # Web scraping
import smtlib                    # Server SMTP
# Email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# System date and time manipulation
import datetime

nowDate = datetime.datetime.now()
content = ''                      # Email content placeholder

# Function to extract a list of words in Wikitionary 
def extract_words(url):
    print('Scraping...')
    cnt = ''
    cnt += ('<b>Wiktionary list of words:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.findall('li', atrrs={'class':''})):
        cnt += ((str(i+1)+' :: '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text!='(poprzednia strona)' else '')
    return cnt

cnt = extract_words("https://pl.wiktionary.org/wiki/Kategoria:angielski_(indeks)")
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

# Process of sending email
print('I am creating your email...')
SERVER = 'smptp.gmail.com'          # SMPT server (in this case is Google Gmail)
PORT = 587                          # Gmail is listening on 587 port
FROM = ''                           # Email sender id
TO = ''                             # Email receiver id
PASS = ''                           # Email password

# Creating a text message
msg = MIMEMultipart()
msg['Subject'] = 'Wiktionary List of Words [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(
    now.year)
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content, 'html'))

# Server initiating 
print("Starting Server...")
server = smtlib.SMPT(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendemail(FROM, TO, msg.as_string())
print('Email has been sent')
server.quit()
