import urllib2, urllib
import json
import MySQLdb

def http_get(url):
    url = "http://127.0.0.1:8000/" + url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    result = response.read()
    return result

def http_post(url, data):
    url = 'http://127.0.0.1:8000/' + url
    urldata = urllib.urlencode(data)
    request = urllib2.Request(url, urldata)
    response = urllib2.urlopen(request)
    result = response.read()
    return result

def http_put(url, data):
    url = 'http://127.0.0.1:8000/' + url
    urldata = urllib.urlencode(data)
    request = urllib2.Request(url, urldata)
    request.get_method = lambda:'PUT'
    response = urllib2.urlopen(request)
    result = response.read()
    return result

def http_patch(url, data):
    url = 'http://127.0.0.1:8000/' + url
    urldata = urllib.urlencode(data)
    request = urllib2.Request(url, urldata)
    request.get_method = lambda:'PATCH'
    response = urllib2.urlopen(request)
    result = response.read()
    return result

def http_delete(url):
    url = 'http://127.0.0.1:8000/' + url
    request = urllib2.Request(url)
    request.get_method = lambda:'DELETE'
    response = urllib2.urlopen(request)
    result = response.read()
    return result


def username_to_id(username):
    data = http_get('accounts/')
    json_data = json.loads(data)
    for account in json_data:
        if account['username'] == username:
            return account['id']

