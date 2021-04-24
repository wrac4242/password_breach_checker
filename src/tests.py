'''testing functions'''
import wrac_pwd_checker as wrac
# pylint: disable=W0702

#returns amount failed
def comprimised_pass():
    '''comprimised password testing'''
    failed = 0
    print("Testing comprimised passwords")
    #had to make sure that some passwords were not valid
    passwds = ["password", "123456", "Asddsdsafssdafsasfasf2354243554335"]
    if len(wrac.compromised_passwords(passwds)) != 2:
        print("Comprimised password base test failed")
        failed += 1

    #expects it to crash with 0 len input
    try:
        wrac.compromised_passwords([])
        print("Comprimised passwords failed at 0 len input")
        failed += 1
    except:
        pass
    return failed
