import requests, sys, datetime
from tqdm import tqdm
from prettytable import PrettyTable

def token_price(token, api_url):
    headers = {"Authorization": "Bearer %s" % token}
    url = api_url + 'data/wow/token/?namespace=dynamic-eu&locale=en_GB'
    c = requests.get(url, headers=headers)

    if c.status_code == 200:
        data = c.json()
        return data['price']
    else:
        print('[ERROR] %i' % c.status_code)
