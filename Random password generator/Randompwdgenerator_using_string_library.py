# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:46:27 2020

@author: mohammed ashraf
"""
import random
import string

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

print ("Generating a Randon alphanumeric ")
num = int(input("Enter the Size of the possword you want:"))
print ("Your password is:  ", randomStringDigits(num))

