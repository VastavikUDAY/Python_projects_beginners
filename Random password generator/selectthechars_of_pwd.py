import random

char1 = 'ASDFGHJKLZXCVBNMQWERTYUIOP'
char2 = 'asdfghjklzxcvbnmqwertyuiop'
char3 ='123456789'
char4 = '!@#$%^&*'


print("-------------Select the characters You want in your password------------------")
print("Enter 1 for yes and 0 for no")
new = ''
option1 = int(input("Do you want to add uppercase:"))
if option1 == 1:
    new = new+char1
option2 = int(input("Do you want to add lowercase:"))
if option2 == 1:
    new = new+char2
option3 = int(input("Do you want to add number:"))
if option3 == 1:
    new = new+char3
option4 = int(input("Do you want to add special characters:"))
if option4 == 1:
    new = new+char4

number = int(input("Number of chars::"))
password = ''
for p in range(number):
    password +=random.choice(new)
print(password)