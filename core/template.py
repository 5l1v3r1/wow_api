import requests, sys, datetime
from tqdm import tqdm
from prettytable import PrettyTable

def character_feed(token, api_url, realm, character):
    start = datetime.datetime.now()
    r = 0

    table = PrettyTable(['Name', 'id', 'Connected realm','Timezone', 'Status', 'Population', 'Has que']) # Header
    table.align = "l" # Text Align left

    headers = {"Authorization": "Bearer %s" % token}
    url = api_url + 'wow/character/magtheridon/zeznzo?fields=feed&locale=en_GB'
    c = requests.get(url, headers=headers)

    if c.status_code == 200:
        data = c.json()

        # format data from here.
        #print(data) # Show all data

    else:
        print('[ERROR] %i' % c.status_code)
        sys.exit(1)
