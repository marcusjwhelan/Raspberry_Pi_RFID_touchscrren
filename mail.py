"""
        Written By Marcus Whelan for Senior design 1 project 2
        This file is how emails are sent to the user
"""
#!/usr/bin/python
import smtplib
import mimetypes
import email
import email.mime.application
import sys

def sendImage(path):
    #send params
    msg=email.mime.Multipart.MIMEMultipart()
    msg['Subject'] = "Picture from PI"
    msg['From'] = "mjwthunder@gmail.com"
    msg['To'] = "marcus.j.whelan@gmail.com"
    #body
    body = email.mime.Text.MIMEText("""Hello World""")
    msg.attach(body)

    #get file path
    directory = path

    #split to get filename
    spl_dir=directory.split('/')
    filename=spl_dir[len(spl_dir)-1]

    #split to get type
    spl_type=directory.split('.')
    type=spl_type[len(spl_type)-1]

    #Attach it
    fp=open(directory,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype=type)
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)

    # send via gmail
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login('mjwthunder@gmail.com','thunder123')
    s.sendmail('mjwthunder@gmail.com','marcus.j.whelan@gmail.com',msg.as_string())
    s.quit()

def sendXL(path,receiverEmail):    
    #get file path
    directory = path

    #split to get filename
    spl_dir=directory.split('/')
    filename=spl_dir[len(spl_dir)-1]

    #split to get type
    spl_type=directory.split('.')
    type=spl_type[len(spl_type)-1]

    #send params
    msg=email.mime.Multipart.MIMEMultipart()
    msg['Subject'] = filename
    msg['From'] = "mjwthunder@gmail.com"
    msg['To'] = receiverEmail
    #body
    body = email.mime.Text.MIMEText("""Here is the excel file from your class.""")
    msg.attach(body)
    
    #Attach it
    fp=open(directory,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype=type)
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)

    # send via gmail
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login('mjwthunder@gmail.com','thunder123')
    s.sendmail('mjwthunder@gmail.com',receiverEmail,msg.as_string())
    s.quit()




















    
