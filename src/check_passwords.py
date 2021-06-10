import wrac_pwd_checker as wrac
from sys import stdin

# some quick code cobbled together
# takes in passwords from stdin and outputs comprimised ones on stdout

passwds = []

for line in stdin:
  passwds.append(line.rstrip())

print(wrac.compromised_passwords(passwds))
