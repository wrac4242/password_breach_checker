'''testing functions'''
import wrac_pwd_checker as wrac
# noqa: E722
# pylint: disable=W0702

#returns amount failed
def comprimised_pass():
    '''comprimised password testing'''
    failed = 0
    print("Testing comprimised passwords")
    #had to make sure that some passwords were not valid
    try:
        passwds = ["password", "123456", "Asddsdsafssdafsasfasf2354243554335"]
        if len(wrac.compromised_passwords(passwds)) != 2:
            print("Comprimised password base test failed")
            failed += 1
    except:
        print("comprimised password error")
        failed += 1

    #expects it to crash with 0 len input
    try:
        wrac.compromised_passwords([])
        print("Comprimised passwords failed at 0 len input")
        failed += 1
    except:
        pass
    return failed


def pass_gen():
    '''password generator testing'''
    failed = 0

    #test output size
    try:
        amount = 4
        length = 11
        pass_generated = wrac.password_generator(length, amount)
        if len(pass_generated) != amount:
            print("amount created not equal")
            failed += 1
        for i in pass_generated:
            if len(i) != length:
                print("password length not equal")
                failed += 1
    except:
        failed += 1

    #test if amount is not required
    try:
        wrac.password_generator("15")
    except:
        print("amount given required, should not")
        failed += 1

    #test input sterilisation
    try:
        wrac.password_generator("a")
        print("Length not sterilised")
        failed += 1
    except:
        pass

    try:
        wrac.password_generator(10, "a")
        print("amount not sterilised")
        failed += 1
    except:
        pass

    #check minimum length
    try:
        wrac.password_generator(1)
        print("Minimum length failed")
        failed += 1
    except:
        pass

    return failed


def test_all():
    '''test using all test cases'''
    failed_count = 0
    failed_count += comprimised_pass()
    failed_count += pass_gen()
    print("{} failiures".format(failed_count))


if __name__ == "__main__":
    test_all()
