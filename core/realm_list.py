import requests, sys, datetime
from tqdm import tqdm
from prettytable import PrettyTable

def realm_list(token, api_url, realm_status, namespace, local):
    start = datetime.datetime.now()
    r = 0

    table = PrettyTable(['Name', 'id', 'Connected realm','Timezone', 'Status', 'Population', 'Has que']) # Header
    table.align = "l" # Text Align left

    headers = {"Authorization": "Bearer %s" % token}
    url = api_url + 'data/wow/realm/?namespace=%s&locale=%s' % (namespace, local)
    c = requests.get(url, headers=headers)

    if c.status_code == 200:
        data = c.json()
        for realm in range(len(data['realms'])):
            name = data['realms'][int(realm)]['name']
            id = data['realms'][int(realm)]['id']
            connected_realm = data['realms'][int(realm)]['key']['href'].split('/')[-1].split('?')[0]

            if realm_status == True:
                try:
                    # Gather realm data such as que, timezone and more
                    url2 = api_url + 'data/wow/connected-realm/%i?namespace=%s&locale=%s' % (id, namespace, local)
                    a = requests.get(url2, headers=headers)
                    data2 = a.json()
                    que = data2['has_queue']
                    status = data2['status']['type']
                    population = data2['population']['type']
                    timezone = data2['realms'][0]['timezone']

                except Exception as e:
                    que = 'Error'
                    status = 'Error'
                    population = 'Error'
                    timezone = 'Error'
            else:
                que = 'No data'
                status = 'No data'
                population = 'No data'
                timezone = 'No data'


            table.add_row([name, id, connected_realm, timezone, population, status, que])
            table.sortby = "Name"
            r+=1

        print(table)
        print('Found %i results in %s' % (int(r), datetime.datetime.now()-start))
    else:
        print('[ERROR] %i' % c.status_code)
