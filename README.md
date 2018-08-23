# World of warcraft API

***


Installation:

1) Register on: https://dev.battle.net.

2) Login and go to: https://dev.battle.net/apps/mykeys

3) Create a new key and fill out the forum.

4) Put your API secret and key in "auth.py"

5) You're all set. you can now use main.py.


```Shell
apt install python3-pip
```

```Shell
pip3 install -r requirements.txt
```


Linux:
```Shell
chmod +x main.py
./main.py -h
```

Windows:
```Shell
py main.py -h
```

Usage:
```Shell
usage: main.py [-h] [-s SET_REGION] [-r SET_REALM] [-tp] [-rl] [-rs] [-st]

                                    WoW API Data Gatherer

                                    Register for API on:
                                    https://dev.battle.net/

                        ------------------------------------------------

                        ╦ ╦┌─┐┬─┐┬  ┌┬┐  ┌─┐┌─┐  ╦ ╦┌─┐┬─┐┌─┐┬─┐┌─┐┌─┐┌┬┐
                        ║║║│ │├┬┘│   ││  │ │├┤   ║║║├─┤├┬┘│  ├┬┘├─┤├┤  │
                        ╚╩╝└─┘┴└─┴─┘─┴┘  └─┘└    ╚╩╝┴ ┴┴└─└─┘┴└─┴ ┴└   ┴
                                            ╔═╗╔═╗╦
                                            ╠═╣╠═╝║
                                            ╩ ╩╩  ╩

optional arguments:
  -h, --help            show this help message and exit
  -s SET_REGION, --set-region SET_REGION
                        Set region to EU, US or CN, default is EU. Ex: main.py
                        -s us
  -r SET_REALM, --set-realm SET_REALM
                        Set Realm. Ex: main.py -r magtheridon
  -tp, --token-price    Show wow token gold price for given region. ex:
                        main.py -s us -t
  -rl, --realm-list     List all realms
  -rs, --show-realm-status-all
                        List all realms and show status data
  -st, --show-realm-status
                        Show status data for given realm

```


No need to set a region if you're EU. EU is the default region.
