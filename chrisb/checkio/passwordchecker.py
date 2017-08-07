#!/usr/bin/python

import re

def checkio(data):
    if len(data) <= 10:
        if re.match("[a-z]+", data):
            if re.match("[A-Z]+", data):
                if re.match("[0-9]+", data):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
