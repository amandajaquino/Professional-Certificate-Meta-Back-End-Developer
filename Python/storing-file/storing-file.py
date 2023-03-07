""" import random
f = open("petname.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list)) """


import random
f_name = input('Type the file name: ')
f = open("petname.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))