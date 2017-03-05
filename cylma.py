#!/usr/bin/env python3

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv, exit
from getopt import getopt
from json import dumps, loads

__author__  = 'nigella'
__version__ = '0.0.2-dev'

SHODAN_API_KEY = ''
UA_API_KEY     = ''

# Useless functions

def flag(): print('\n\t\t\t\t\t     ▄▄·  ▄· ▄▌▄▄▌  • ▌ ▄ ·.  ▄▄▄·\n\t\t\t\t\t     ▐█ ▌▪▐█▪██▌██•  ·██ ▐███▪▐█ ▀█\n\t\t\t\t\t     ██ ▄▄▐█▌▐█▪██▪  ▐█ ▌▐▌▐█·▄█▀▀█\n\t\t\t\t\t     ▐███▌ ▐█▀·.▐█▌▐▌██ ██▌▐█▌▐█ ▪▐▌\n\t\t\t\t\t     ·▀▀▀   ▀ • .▀▀▀ ▀▀  █▪▀▀▀ ▀  ▀\n\n\t\t\t\t\t     nigella. twttr: @_ngll gh: @nig\n')
def usage(): print('\n\n\n\t\t\t\t\t\t\t  USAGE    \n\t\t\t\t\t\t\t  =====\n\n\t\t\t\t\t\t  FLAG -i, --ip-address\n\t\t\t\t\t\t  FLAG -u, --user-agent\n\n\t\t\t\t\t     P.S. python(3) cylma.py <flags>\n\n'); exit()


def create_json(ip_data=None, shodan_data='None', ua_data=None):
    ' Create JSON data from given variables '

    # IP API ERROR HANDLING

    if ip_data == None: ip_data, ip_api_status = 'None', 'None'

    elif ip_data != None:
        if ip_data['status'] == 'fail': ip_data, ip_api_status = ip_data['message'], 'error'
        else: ip_api_status = 'success'


    # USER-AGENT API ERROR HANDLING

    if ua_data == None: ua_data, ua_api_status = 'None', 'None'

    elif ua_data != None:
        if 'error' in ua_data: ua_data, ua_api_status = ua_data['error']['message'], 'error'
        else: ua_api_status = 'success'


    # SHODAN API ERROR HANDLING

    if shodan_data == 'None': shodan_api_status, shodan_data = 'None', 'None'

    elif shodan_data != None:
        if 'error' in shodan_data: shodan_data, shodan_api_status = shodan_data['error'], 'error'
        else: shodan_api_status = 'success'

    else: shodan_api_status, shodan_data = 'error', 'error_occured'


    data = {
        "ip_api": ip_api_status,
        "ip_data": [ip_data],
        "ua_api": ua_api_status,
        "ua_data": [ua_data],
        "shodan_api": shodan_api_status,
        "shodan_data": [shodan_data],
        "author": "nigella",
        "author_data": [{"twitter": "@_ngll", "github": "@nig"}],
        "last_words": [
            "An old friend once told me something that gave me great comfort.",
            "Something he read. He said Mozart, Beethoven and Chopin never died.",
            "They simply became music."
        ]
    }

    with open('data.json', 'w') as datas: datas.writelines(dumps(data, indent=4 * ' '))


def create_request(URL, values=None, hds='Cylma - nigella is watching'):
    ' Create new request '

    request = Request(
                URL,           # Use HTTP, maybe user doesn't have up-to-date SSL certificate.
                data = values, # Default is none, if you want to change it, be sure you know what are you doing.
                headers = {    # Default is just User-Agent, but you can use other headers too.
                            'User-Agent': hds
                        }
            )

    return request


def open_request(request):
    ' Open given request '

    try: return loads(urlopen(request).read())
    except: pass


def ip_analysis(ip, shodan=True, ip_api=True):
    ' Shodan API & IP-API '

    global ip_data, shodan_data

    if shodan:
        shodan_data = open_request(
            create_request('https://api.shodan.io/shodan/host/{0}?key={1}'.format(ip, SHODAN_API_KEY))
        )

    if ip_api:
        ip_data = open_request(
            create_request('http://ip-api.com/json/{0}?fields=254233'.format(ip))
        )


def ua_analysis(ua):
    ' User-Agent API '

    global ua_data

    ua_data = open_request(
        create_request('https://useragentapi.com/api/v4/json/{0}/{1}'.format(UA_API_KEY, ua))
    )


if __name__ == '__main__':
    ' When script is started mainly (directly) '

    flag()

    try: opts, args = getopt(argv[1:], 'hi:u:', ['ip-address=', 'user-agent='])
    except: usage() # When bad argument typed

    for opt, arg in opts:
        if opt == '-h': usage()
        elif opt in ('-i', '--ip-address'): ip = arg
        elif opt in ('-u', '--user-agent'): ua = urlencode({"Agent": arg}).split('Agent=')[1]

    try:
        if opt: ''
    except: usage() # When there is no arguments

    # UN-USED ARGUMENTS ERROR HANDLING

    try: ip_analysis(ip)
    except: ip_data, shodan_data = None, 'None'

    try: ua_analysis(ua)
    except: ua_report = None

    create_json(ip_data=ip_data, shodan_data=shodan_data, ua_data=ua_data) # Create final JSON data

else: print('Well.. You can use this script in yours but, you\'ll be suffer.') # When script is started from another one
