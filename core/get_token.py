import requests, sys, datetime
from tqdm import tqdm
from prettytable import PrettyTable

def get_token(region, key, secret, bnet_url):
    payload = {"client_id": "%s" % key, "client_secret": "%s" % secret, "grant_type": "client_credentials"}
    get = requests.post(bnet_url + '/oauth/token', data=payload)

    data = get.json()

    if get.status_code == 200:
        return data['access_token']
        print('[OK] Got token successfully')
    else:
        print('[%i] Failed to get token' % get.status_code)
        sys.exit(1)
