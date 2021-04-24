"""
module that utilizes haveibeenpwned to give lists of compromised passwords
"""
from hashlib import sha1
import requests

URL = "https://api.pwnedpasswords.com/range/"
PARAMETERS = {"user-agent":"wrac_password_checker"}

#makes hash
#credit where credit is due https://gist.github.com/re4lfl0w/a6ff3a988b4e67297efc
def _make_sha1(initem, encoding='utf-8'):
    return sha1(initem.encode(encoding)).hexdigest()

#returns hash list
def _make_requests(hash_5):
    request = requests.get(URL+str(hash_5), params=PARAMETERS)
    returning = []
    for i in request.text.split("\r\n"):
        returning.append(i[:35])
    return returning

def compromised_passwords(passwords):
    '''returns a list of compromised passwords from a list of passwords to test'''
    hash_list = []
    to_send = []
    for i in passwords:
        hashed = _make_sha1(i, encoding='utf-8')
        hash_list.append(hashed)
        to_send.append(hashed[:5])
    to_send = list(set(to_send))
    recived = []
    for i in to_send:
        recived.extend(_make_requests(i))
    compromised = []
    #check if hashes are in list
    for i in range(len(hash_list)):
        if hash_list[i].upper()[5:] in recived:
            compromised.append(passwords[i])
    return compromised
