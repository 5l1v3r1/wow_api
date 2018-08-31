import requests, sys, datetime
from tqdm import tqdm
from prettytable import PrettyTable

def realm_status(token, api_url, realm, namespace, local):
    start = datetime.datetime.now()
    r = 0

    table = PrettyTable(['Name', 'id', 'Connected realm', 'Timezone', 'Category', 'Type', 'Has queue', 'Population']) # Header
    table.align = "l" # Text Align left

    headers = {"Authorization": "Bearer %s" % token}
    # Url for name search and some other data
    url = api_url + 'data/wow/realm/%s?namespace=%s&locale=%s' % (realm, namespace, local)
    c = requests.get(url, headers=headers)

    if c.status_code == 200:
        data = c.json()

        try:
            # Gather realm data such as que, timezone and more
            name = data['name']
            id = data['id']
            connected_realm = data['connected_realm']['href'].split('/')[-1].split('?')[0]
            type = data['type']['name']
            category = data['category']
            timezone = data['timezone']

            # Url for realm que and population status and more...
            url2 = api_url + 'data/wow/connected-realm/' + connected_realm + '?namespace=' + namespace + '&locale=' + local
            b = requests.get(url2, headers=headers)
            data2 = b.json()
            que = data2['has_queue']
            population = data2['population']['name']

        except Exception as e:
            print(e)
            que = 'Error'
            type = 'Error'
            timezone = 'Error'
            category = 'Error'
            id = 'Error'
            que = 'Error'
            population = 'Error'
            name = realm

        table.add_row([name, id, connected_realm, timezone, category, type, que, population])

        print(table)
    else:
        print('[ERROR] %i' % c.status_code)
