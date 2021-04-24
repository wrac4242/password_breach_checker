"""
module that utilizes haveibeenpwned to give lists of compromised passwords
"""
import private_functions as priv
import errors as err

URL = "https://api.pwnedpasswords.com/range/"
PARAMETERS = {"user-agent":"wrac_password_checker"}

def compromised_passwords(passwords):
    '''returns a list of compromised passwords from a list of passwords to test'''
    if len(passwords) <= 0:
        raise err.ArgsTooSmallError("passwords to check should be longer")

    hash_list = []
    to_send = []
    for i in passwords:
        hashed = priv.make_sha1(i, encoding='utf-8')
        hash_list.append(hashed)
        to_send.append(hashed[:5])
    to_send = list(set(to_send))
    recived = []
    for i in to_send:
        recived.extend(priv.make_requests(i, URL, PARAMETERS))
    compromised = []
    #check if hashes are in list
    # pylint: disable=consider-using-enumerate
    for i in range(len(hash_list)):
        if hash_list[i].upper()[5:] in recived:
            compromised.append(passwords[i])
    return compromised


def password_generator(length, amount):
    '''generates amount passwords of a given character length'''
