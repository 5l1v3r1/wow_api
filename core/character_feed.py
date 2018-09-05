import requests, sys, datetime
from tqdm import tqdm
from prettytable import PrettyTable

def character_feed(key, api_url, realm, character, local):
    start = datetime.datetime.now()
    r = 0

    table = PrettyTable(['Type', 'Title', 'Item ID', 'Context', 'Description']) # Header
    table.align = "l" # Text Align left

    #headers = {"Authorization": "Bearer %s" % token}
    url = api_url + 'wow/character/' + realm + '/' + character + '?fields=feed&locale=' + local + '&apikey=' + key
    c = requests.get(url)

    if c.status_code == 200:
        data = c.json()

        for feed in range(len(data['feed'])):
            type = data['feed'][int(feed)]['type']
            if type == "ACHIEVEMENT":
                title = data['feed'][int(feed)]['achievement']['title']
                description = data['feed'][int(feed)]['achievement']['description']
                if len(description) > 50:
                    description = description[:50] + '...'
                itemid = ''
                context = ''
            elif type == "LOOT":
                itemid = data['feed'][int(feed)]['itemId']
                context = data['feed'][int(feed)]['context']
                description = ''
                title = ''
            elif type == "BOSSKILL":
                title = data['feed'][int(feed)]['achievement']['title']
                description = ''
                itemid = ''
                context = ''
            elif type == "CRITERIA":
                title = data['feed'][int(feed)]['achievement']['title']
                description = data['feed'][int(feed)]['achievement']['description']
                if len(description) > 50:
                    description = description[:50] + '...'
                itemid = ''
                context = ''

            table.add_row([type, title, itemid, context, description])

        print(table)


    else:
        print('[ERROR] %i' % c.status_code)
        sys.exit(1)
