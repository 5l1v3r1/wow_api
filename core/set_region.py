def set_region(region):
    if args.set_region:
        if args.set_region == 'eu'.upper():
            bnet_url = "https://eu.battle.net/"
            api_url = "https://eu.api.battle.net/"
        elif args.set_region == 'us'.upper():
            bnet_url = "https://us.battle.net/"
            api_url = "https://us.api.battle.net/"
        elif args.set_region == 'cn'.upper():
            bnet_url = "https://cn.battle.net/"
            api_url = "https://cn.api.battle.net/"
        else:
            print('[ERROR] Valid regions are: US, EU, CN and the default region is EU.')
    else:
        args.set_region = 'eu'.upper()
        bnet_url = 'https://eu.battle.net/'
        api_url = "https://eu.api.battle.net/"
