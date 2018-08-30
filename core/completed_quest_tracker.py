import requests, sys, datetime
from tqdm import tqdm
from prettytable import PrettyTable

def completed_quest_tracker(key, api_url, realm, character, id):

    table = PrettyTable(['Character', 'Realm', 'Title', 'id', 'Status']) # Header
    table.align = "l" # Text Align left

    #headers = {"Authorization": "Bearer %s" % token}
    url = api_url + 'wow/character/' + realm + '/' + character + '?fields=quests&locale=en_GB&apikey=' + key
    c = requests.get(url)

    if c.status_code == 200:
        data = c.json()

        url2 = 'https://wowhead.com/quest=' + str(id)
        b = requests.get(url2)

        name = b.url.split('/')[-1].replace('-', ' ')

        if int(id) in data['quests']:
            status = 'Completed'
        else:
            status = 'Not Completed'

        table.add_row([character, realm, name, id, status])
        print(table)

    else:
        print('[ERROR] %i' % c.status_code)
        sys.exit(1)
