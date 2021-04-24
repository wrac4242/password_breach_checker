import requests

from hashlib import sha1
URL = "https://api.pwnedpasswords.com/range/"
PARAMETERS = {"user-agent":"wrac_password_checker"}

#makes hash
def _make_sha1(s, encoding='utf-8'):
	return sha1(s.encode(encoding)).hexdigest()

#returns hash list
def _make_requests(hash_5):
	r = requests.get(URL+str(hash_5), params=PARAMETERS)
	returning = []
	for i in r.text.split("\r\n"):
		returning.append(i[:35])
	return returning

def compromisedPasswds(passwords):
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
	compromised_passwords = []
	#check if hashes are in list
	for i in range(len(hash_list)):
		if hash_list[i].upper()[5:] in recived:
			compromised_passwords.append(passwords[i])
			print("Hash:", hash_list[i],"found")
			print("password:", passwords[i],"found, please regen")
	return compromised_passwords
    
