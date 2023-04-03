import re
string1 = 'abcd1234'

x = re.search('[0-9]', string1)
if x != None:
    print(True)
else:
    print(False)

string2 = 'ABCD'

y = re.search('[a-z]', string2)
if y != None:
    print(True)
else:
    print(False)

password = 'ABC(@!234'
symbols = re.search('[!@#$%^&*-+]', password)
capital = re.search('[A-Z]', password)
number = re.search('[0-9]', password)
if symbols == None:
    print("You must use special character in password")
else:
    print('pass')

if capital == None:
    print('You must use capital letters')
else:
    print('pass')
if number == None:
    print('You must use numbers')
else:
    print('pass')

