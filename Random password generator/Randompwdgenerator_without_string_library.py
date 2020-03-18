import random

chars = "asdfghjklqwertyuiopzxcvbnm123456789ASDFGHJKLZXCVBNMQWERTYUIO!@#$%^&*"

num =int(input("Number of chars::"))

password =''
for p in range(num):
    password +=random.choice(chars)
print(password)