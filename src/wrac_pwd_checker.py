"""
module that utilizes haveibeenpwned to give lists of compromised passwords
"""
import private_functions as priv
import errors as err

# noqa: E722

PASS_MIN_LEN = 10

URL = "https://api.pwnedpasswords.com/range/"
PARAMETERS = {"user-agent":"wrac_password_checker"}

def compromised_passwords(passwords):
    '''returns a list of compromised passwords from a list of passwords to test'''
    #bad input testing
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


def password_generator(length, amount=1):
    '''generates amount passwords of a given character length'''

    #bad input testing
    #types

    # pylint: disable=raise-missing-from
    try:
        length = int(length)
    except:
        raise err.ValueNotInt("Expected int for length")

    try:
        amount = int(amount)
    except:
        raise err.ValueNotInt("Expected int for amount")

    #length
    if length <= PASS_MIN_LEN:
        raise err.ArgsTooSmallError("password length should be greater than 10")
    if amount <= 0:
        raise err.ArgsTooSmallError("password to generate shoult not be 0")

    return_passes = []
    for _ in range(amount):
        return_passes.append(priv.genpass(length))

    return return_passes
