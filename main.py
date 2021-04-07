import smtplib
from email.message import EmailMessage
import requests
from threading import Timer
from request import getEthPrice

#Useful variables
#Your api key here:
apiKey = '...'
#!!!!Do not use you main e-mail adress
mail ='...'
password = '...'
#Any E-mail adress that accepts unknow sources
to = '...'
#mail Subject
mailSubject = 'Hey !'
#Number of seconds between requests 
time = 300
#crypto currency symbol
symbol = 'BTC'
#outputCurrency
outputCurrency = 'EUR'
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
    price = getEthPrice(symbol,outputCurrency,apiKey)
    ################ ADD your conditions IN HERE ################## 
    if price < 37000:
        message= f"{symbol} price is : {price} {outputCurrency}"
        sendMail(mailSubject,message)
    Timer(time,exe).start()
exe()
