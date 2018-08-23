import requests, sys, datetime
from tqdm import tqdm
from prettytable import PrettyTable

def realm_status(token, api_url, realm):
    start = datetime.datetime.now()
    r = 0

    table = PrettyTable(['Name', 'id', 'Timezone', 'Category', 'Type']) # Header
    table.align = "l" # Text Align left

    headers = {"Authorization": "Bearer %s" % token}
    url = api_url + 'data/wow/realm/%s?namespace=dynamic-eu&locale=en_GB' % realm
    c = requests.get(url, headers=headers)


    if c.status_code == 200:
        data = c.json()

        try:
            # Gather realm data such as que, timezone and more
            name = data['name']
            id = data['id']
            type = data['type']['name']
            category = data['category']
            timezone = data['timezone']

        except Exception as e:
            que = 'Error'
            type = 'Error'
            timezone = 'Error'
            category = 'Error'
            id = 'Error'
            name = realm

        table.add_row([name, id, timezone, category, type])

        print(table)
    else:
        print('[ERROR] %i' % c.status_code)
