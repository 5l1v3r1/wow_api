import requests, sys, datetime
from tqdm import tqdm
from prettytable import PrettyTable

def auction_house_data(api_url, realm, local, key):
    start = datetime.datetime.now()
    r = 0

    table = PrettyTable(['Item id', 'Owner', 'Realm', 'Bid', 'Buyout', 'Quantity', 'Time Left']) # Header
    table.align = "l" # Text Align left

    #headers = {"Authorization": "Bearer %s" % token}
    url = api_url + 'wow/auction/data/' + realm + '?locale=' + local + '&apikey=' + key

    url2 = api_url + 'wow/auction/data/magtheridon?locale=en_GB&apikey=m7raxcdhbtdrugqfdrwa3eav9vthhzv5'
    c = requests.get(url)

    if c.status_code == 200:
        data = c.json()
        url = data['files'][0]['url']
        b = requests.get(url)
        data = b.json()

        # Load all auctions
        for auction in range(len(data['auctions'])):
            id = data['auctions'][int(auction)]['item']
            owner = data['auctions'][int(auction)]['owner']
            realm = data['auctions'][int(auction)]['ownerRealm']
            bid = data['auctions'][int(auction)]['bid']
            buyout = data['auctions'][int(auction)]['buyout']
            quantity = data['auctions'][int(auction)]['quantity']
            timeleft = data['auctions'][int(auction)]['timeLeft']

            # Get item name from WoWHead (Slows down the process massively)
            #url2 = 'https://wowhead.com/item=' + str(id)
            #d = requests.get(url2)

            #name = d.url.split('/')[-1].replace('-', ' ')

            table.add_row([id, owner, realm, bid, buyout, quantity, timeleft])
        print(table)

    else:
        print('[ERROR] %i' % c.status_code)
        print(c.text)
        sys.exit(1)
