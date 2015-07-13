from lib import tools
import json

data = tools.http_get('accounts/')
def name(data):
    jsondata = json.loads(data)
    for account in jsondata:
        if account['username'] == 'llll':
            print account['id']
