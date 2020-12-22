import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sense_hat import SenseHat
import time
from random import randint
from pathlib import Path
import os
import configparser

def do_send_email(frm, to, pwd, smtpserver, smtpport, message, subject):
    msg = MIMEMultipart()
    msg['From'] = frm
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()
    smtpclient = smtplib.SMTP(smtpserver, smtpport)
    smtpclient.starttls()
    print(f'\nEmail content:\n{text}')
    smtpclient.login(frm, pwd)
    smtpclient.sendmail(frm, to, text)
    smtpclient.quit()

def send_email(subject, message):
    configParser = configparser.RawConfigParser()
    configFilePath = os.getenv('HOME') + '/.ssh/weather.cfg'
    configParser.read(configFilePath)
    frm = configParser.get('Email', 'from')
    to = configParser.get('Email', 'to')
    pwd = configParser.get('Email', 'password')
    server = configParser.get('Email', 'server')
    port = configParser.get('Email', 'port')
    do_send_email(frm, to, pwd, server, port, message, subject)

def do_email_weather(sense):
    temperature = round(sense.get_temperature() * 1.8 + 32, 1)
    pressure = round(sense.get_pressure(), 1)
    humidity = round(sense.get_humidity(), 1)
    message = f'T={temperature}F, H={humidity}, P={pressure}'
    subject = 'Temperature from Raspberry Pi 4'
    print(f'Subject: {subject}\nmessage: {message}')
    send_email(subject, message)

def email_weather():
    sense = SenseHat()
    sense.clear()
    do_email_weather(sense)
    time.sleep(1)
    sense.clear()

def main():
    for i in range(1):
        email_weather()

if __name__ == '__main__':
    main()
