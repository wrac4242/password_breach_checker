import wrac_pwd_checker as wrac

from sys import stdin

passwds = []

for line in stdin:
  passwds.append(line.rstrip())

print(wrac.compromised_passwords(passwds))
