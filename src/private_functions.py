'''private functions'''
from hashlib import sha1
import requests

#credit where credit is due https://gist.github.com/re4lfl0w/a6ff3a988b4e67297efc
def make_sha1(initem, encoding='utf-8'):
    '''makes sha1 hash'''
    return sha1(initem.encode(encoding)).hexdigest()

#returns hash list
def make_requests(hash_5, url, parameters):
    '''returns hash list'''
    request = requests.get(url+str(hash_5), params=parameters)
    returning = []
    for i in request.text.split("\r\n"):
        returning.append(i[:35])
    return returning
