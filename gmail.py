# This script is written for use inside python scripts so I can be notified of progress, completion, or failures. It allows me to set complex jobs to run without the need to babysit them. Probably the most important evolution in my business process. 
# Secrets is a file saved in the python install directory with variable definitions you do not want embedded in your code. Making this file is up to you. 
import smtplib, secrets
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def MailAlert(msg):
    # For applications where you want to send a quick message using code. Not flexible but not verbose in its implementation. Limited to a single recipient.  
    fromaddr = secrets.email_g
    toaddrs  = secrets.email_g
    # Credentials (if needed)
    username = secrets.gname
    password = secrets.gpass
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

def sendMail(fromMail,toMail,subj,msg_body):
    #For applications where you want to send a quick message using code. More Flexible than MailAlert but also more verbose in its implementation. Allows Multiple Recipients as a comma delimited list.
    msg = MIMEMultipart()
    msg["Subject"]=subj
    msg["From"]=fromMail
    msg["To"]=toMail
    body = MIMEText(msg_body)
    msg.attach(body)
    # Credentials (if needed)
    username = secrets.gname
    password = secrets.gpass
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(msg["From"],msg["To"].split(","), msg.as_string())
    server.quit()

def done(msg_body):
    # Sends a quick message reporting a job is done
    msg = MIMEMultipart()
    msg["Subject"]='job complete'
    msg["From"]=secrets.email_g
    msg["To"]=secrets.email_g
    body = MIMEText(msg_body)
    msg.attach(body)
    # Credentials (if needed)
    username = secrets.gname
    password = secrets.gpass
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(msg["From"],msg["To"], msg.as_string())
    server.quit()

def error(msg_body):
    # Sends a quick message reporting a job broke
    msg = MIMEMultipart()
    msg["Subject"]='job error'
    msg["From"]=secrets.email_g
    msg["To"]=secrets.email_g
    body = MIMEText(msg_body)
    msg.attach(body)
    # Credentials (if needed)
    username = secrets.gname
    password = secrets.gpass
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(msg["From"],msg["To"], msg.as_string())
    server.quit()
