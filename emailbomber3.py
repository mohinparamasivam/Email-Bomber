#!/usr/bin/python 3.9
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!
# Python 3 rewrite by Omicron166

from os import urandom
import os
import smtplib
from getpass import getpass
import getpass
import sys
from time import sleep
import time

print ('                                                                    ')
print ('                                                                    ')

print ('             ')
user = input('Anonymous name : ')
print ('      ')
passwd = getpass('Password: ')
passwd = getpass.getpass('Password: ')

print ('   ')



total = input('Number of send: ')

print ('    ')

Cserver = input('Custom smtp server (leave blank to use gmail): ')

if not server == '':
    stmp_server = Cserver
    Cport = input('Custom smtp port (leave blank to use port 587): '))
    if not Cport == '':
        port = int(Cport)
    else:
        port = 587
else:
    smtp_server = 'smtp.gmail.com'
    port = 587
smtp_server = 'smtp.gmail.com'
port = 587


print ('')

    server.starttls()
    server.login(email, passwd)
    for i in range(1, int(total) + 1):
        subject = urandom(9)
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + '\n' + body
        server.sendmail(email, to, msg)
        print ("\rE-mails sent: %i" % i)
        sleep(1)
        time.sleep(1)
        sys.stdout.flush()
    server.quit()
    print ('\n Done !!!')
except KeyboardInterrupt:
    print ('[-] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print ('\n[!] The username, password or custom STMP server you entered is incorrect.')
    print ('\n[!] The username or password you entered is incorrect.')
    sys.exit()
