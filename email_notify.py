#!/usr/bin/env python3
import os, sys, argparse, datetime, time, smtplib
from auth import key, secret
from core.send_mail import *
from core.get_token import *
from auth import key

banner = '''
                        ╦ ╦┌─┐┬─┐┬  ┌┬┐  ┌─┐┌─┐  ╦ ╦┌─┐┬─┐┌─┐┬─┐┌─┐┌─┐┌┬┐
                        ║║║│ │├┬┘│   ││  │ │├┤   ║║║├─┤├┬┘│  ├┬┘├─┤├┤  │
                        ╚╩╝└─┘┴└─┴─┘─┴┘  └─┘└    ╚╩╝┴ ┴┴└─└─┘┴└─┴ ┴└   ┴
                                            ╔═╗╔═╗╦
                                            ╠═╣╠═╝║
                                            ╩ ╩╩  ╩
'''

def parse_args():
    # Create the arguments
    parser = argparse.ArgumentParser(prog="main.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''\
                                    WoW API Data Gatherer

                                    Register for API on:
                                    https://dev.battle.net/

                        ------------------------------------------------

%s''' % banner)

    # Required
    parser.add_argument("-e", "--set-email", help="Set Email address to mail with")
    #parser.add_argument("-et", "--set-email-to", help="Set Email address to mail to")
    parser.add_argument("-p", "--set-password", help="Set Email password")
    parser.add_argument("-s", "--set-smtp-server", help="Set SMTP server for this Email address")
    parser.add_argument("-sp", "--set-smtp-port", help="Set SMTP server port for this Email address")
    parser.add_argument("-r", "--set-realm", help="Set Realm.")
    parser.add_argument("-c", "--set-character-name", help="Set character name.")
    parser.add_argument("-a", "--set-achievement", help="Set region to EU, US or CN, default is EU.")

    return parser.parse_args()

args = parse_args()

def check(character, realm, achi, key):
    try:
        print('[%s %s] Checking for completion of achievement %s...' % (time.strftime('%d-%m-%Y'),time.strftime('%X'), achi))
        url = api_url + 'wow/character/' + realm + '/' + character + '?fields=feed&locale=en_GB&apikey=' + key
        c = requests.get(url)

        if c.status_code == 200:
            data = c.json()
            for feed in range(3): # Check first 3 achievements
                type = data['feed'][int(feed)]['type']
                if type == "ACHIEVEMENT":
                    title = data['feed'][int(feed)]['achievement']['title']
                    if title == achi:
                        return True

        else:
            print('[ERROR] Failed to find profile for this character on this realm. Exiting...')
            sys.exit(1)
    except Exception as e:
        print('[ERROR] %s' % e); sys.exit(1)


# Use EU as region
bnet_url = 'https://eu.battle.net/'
api_url = 'https://eu.api.battle.net/'

if args.set_achievement:
    print(banner); print('\nServer started... Checking every minute\n')

    while True:
        try:
            # Check for completion
            completion = check(args.set_character_name, args.set_realm, args.set_achievement, key)
            if completion == True:
                # Debug message
                print('[%s %s] Character %s-%s completed achievement %s !! Exiting...' % (time.strftime('%d-%m-%Y'),time.strftime('%X'),
                    args.set_character_name, args.set_realm, args.set_achievement))

                # Send Email to user
                sendmail(args.set_email, args.set_password, args.set_realm, args.set_character_name, args.set_achievement, args.set_smtp_server, args.set_smtp_port)
                exit(0)
            time.sleep(60) # Timeout to check every x seconds for achi completion
        except KeyboardInterrupt:
           print('[-] Canceled')
           sys.exit(0)
        except Exception as e:
            print('[ERROR] Something went wrong: %s' % e)
            sys.exit(1)
