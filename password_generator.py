import random
str = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890@#$*."
passlength = 10
password = "".join(random.sample(str,passlength))
print(password)