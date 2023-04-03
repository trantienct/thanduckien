import re
string1 = 'abcd'

# x = re.search('[0-9]', string1)
#
# string2 = 'ABCDádzza'
# y = re.search('[a-zA-Z]', string1)
# [a-z] -> Khớp tất cả chuỗi có ký tự từ a đến z
# [A-Z] -> Khớp tất cả chuỗi có ký tự từ A đến Z
# [0-9] -> Khớp tất cả chuỗi có chứa số 0 đến 9
# [!@#$%^&*()-+] -> Khớp tất cả chuỗi có chứa 1 trong các ký tự


password = 'abc1'
x = re.search('[0-9A-Z!@#$%^&*()+]', password)
if x is None:
    print('Your password must be more special')
else:
    print('Pass')
# Password:
# Chứa  ký tự đặc biệt
# Chứa  ký tự in hoa
# Chứa số

# username = 'ABCD1234'
# if re.search('[!@#$%^&*()-+]', username) != None:
#     print("You can't use special character in username")
# else:
#     print('Pass')
# if x != None:
#     print(True)
# else:
#     print(False)
# def checkStringHasNumber(string):
#     result = False
#     for i in string:
#         if i.isnumeric():
#             result = True
#             break
#     return result
# x = checkStringHasNumber(string1)
# print(x)




# string1 = 'abc' #True
string2 = 'abcd12' # False
string3 = '12a' # False

var1 = 'a'

# Loop string -> return true if any character is numeric

# print(string2.isnumeric())
