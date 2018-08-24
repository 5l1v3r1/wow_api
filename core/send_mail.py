#!/usr/bin/env python3
import os, smtplib, getpass, sys

def sendmail(email, passwd, realm, character, achi, smtp, port):
    to = email # Send to sender

    body = '''
Dear %s,

I'm happy to notify you player %s-%s now unlocked achievement %s

Kind regards,

Zeznzo
https://leonvoerman.nl
    ''' % (email, character, realm, achi)

    try:
        server = smtplib.SMTP(smtp.strip(), port)
        server.ehlo()
        server.starttls()
        server.login(email,passwd)
        subject = 'Achievement %s completed by %s-%s' % (achi, character, realm)
        msg = 'From: ' + email + '\nSubject: ' + subject + '\n' + body
        server.sendmail(email,to,msg) # Send message
        server.quit()

    except smtplib.SMTPAuthenticationError:
       print('[ERROR] Email Username or password is incorrect')
       sys.exit(1)
    except Exception as e:
        print('[ERROR] %s' % e); sys.exit(1)
