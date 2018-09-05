#!/usr/bin/env python3
import os, sys, requests, argparse, datetime, textwrap
from auth import key, secret
from tqdm import tqdm
from prettytable import PrettyTable

# Import modules
from core.get_token import *
from core.realm_list import *
from core.set_region import *
from core.token_price import *
from core.realm_status import *
from core.character_feed import *
from core.completed_quest_tracker import *
from core.auction_house_data import *

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
    parser.add_argument("-s", "--set-region", help="Set region to eu, us, kr or tw, default is EU. Ex: main.py -s us")
    parser.add_argument("-r", "--set-realm", help="Set Realm. Ex: main.py -r magtheridon")
    parser.add_argument("-c", "--set-character-name", help="Set character name. Ex: main.py -r magtheridon -c zeznzo -cf")

    # Global
    parser.add_argument("-tp", "--token-price", action="store_true",help="Show wow token gold price for given region. ex: main.py -s us -t")

    # Realms
    parser.add_argument("-rl", "--realm-list", action="store_true", help="List all realms")
    parser.add_argument("-rs", "--show-realm-status-all", action="store_true", help="List all realms and show status data")
    parser.add_argument("-st", "--show-realm-status", action="store_true", help="Show status data for given realm")

    # Character
    parser.add_argument("-cf", "--character-feed", action="store_true", help="Show character feed. Required fields: Realm and Character")
    parser.add_argument("-cq", "--check-quest-completion", help="Check a quest ID if completed. You can find the ID in the WoWHead link. Ex: main.py -r magtheridon -c zeznzo -cq 40983")

    # Guild

    # AH
    parser.add_argument("-ah", "--auction-house-data", action="store_true", help="Dump all auction house data from given realm. Ex: main.py -r magtheridon -ah")

    return parser.parse_args()
args = parse_args()

if args.set_region:
    if args.set_region == 'eu'.lower():
        bnet_url = "https://eu.battle.net/"
        api_url = "https://eu.api.battle.net/"
        namespace = 'dynamic-eu'
        local = 'en_GB'
    elif args.set_region == 'us'.lower():
        bnet_url = "https://us.battle.net/"
        api_url = "https://us.api.battle.net/"
        namespace = 'dynamic-us'
        local = 'en_US'
    elif args.set_region == 'tw'.lower():
        bnet_url = "https://tw.battle.net/"
        api_url = "https://tw.api.battle.net/"
        namespace = 'dynamic-tw'
        local = 'ko_KR'
    elif args.set_region == 'kr'.lower():
        bnet_url = "https://kr.battle.net/"
        api_url = "https://kr.api.battle.net/"
        namespace = 'dynamic-kr'
        local = 'ko_KR'
    else:
        print('[ERROR] Valid regions are: US, EU, CN and the default region is EU.')
else:
    args.set_region = 'eu'.upper()
    bnet_url = 'https://eu.battle.net/'
    api_url = "https://eu.api.battle.net/"
    namespace = 'dynamic-eu'
    local = 'en_GB'

# Grab token
token = get_token(api_url, key, secret, bnet_url)

if args.realm_list:
    print(banner); realm_list(token, api_url, False, namespace, local)

if args.token_price:
    g = token_price(token, api_url, namespace, local)
    print(banner); print("WoW Token price %s: %i gold (%ik)" % (args.set_region, g // 10000, g // 10000000))

if args.show_realm_status_all:
    print(banner); realm_list(token, api_url, True, namespace, local)

if args.show_realm_status and args.set_realm:
    if not args.set_realm:
        print('Please, set a realm: main.py -r magtheridon -st')

    print(banner); realm_status(token, api_url, args.set_realm, namespace, local)

if args.character_feed and args.set_character_name:
    print(banner); print('Showing Character Feed for: %s\n' % args.set_character_name); character_feed(key, api_url, args.set_realm, args.set_character_name, local)

if args.check_quest_completion and args.set_realm and args.set_character_name:
    print(banner); completed_quest_tracker(key, api_url, args.set_realm, args.set_character_name, args.check_quest_completion, local)

if args.auction_house_data and args.set_realm:
    print(banner); auction_house_data(api_url, args.set_realm, local, key)
