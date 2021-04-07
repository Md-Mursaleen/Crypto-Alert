import smtplib
from email.message import EmailMessage
import requests
from threading import Timer
from request import getEthPrice

#Useful variables
#!!!!Do not use you main e-mail adress
mail = 'email'
password = 'mail password'
#Any E-mail adress that accepts unknow sources
to = "your main email"
#mail Subject
mailSubject = 'Hey !'
#Number of seconds between requests 
time = 300
#crypto currency symbol
symbol = 'ETH'
#outputCurrency
outputCurrency = 'USD'
def sendMail(subject,msg):
    try:
        #try to send mail
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(mail,password)
        msgf = EmailMessage()
        msgf.set_content(msg)
        msgf['Subject'] = subject
        msgf['From'] = mail
        msgf['To'] = to
        server.send_message(msgf)
        server.quit()
        print('Mail Sent')
    except:
        #if an erro occurs print this:
        print('an error occured')
#Execution of both functions
def exe():
    price = getEthPrice(symbol,outputCurrency)
    ################ ADD your conditions IN HERE ################## 
    #if .... execute the two lines below 
    message= f"Eth price is : {price} $USD"
    sendMail(mailSubject,message)
    Timer(time,exe).start()
exe()
