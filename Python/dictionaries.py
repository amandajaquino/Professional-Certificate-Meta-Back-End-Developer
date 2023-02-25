#1
""" my_d = {1:'Test', 'Name': 'Jim'}
print(my_d) """
#output:{1: 'Test', 'Name': 'Jim'}

#2
""" my_d = {1:'Test', 'Name': 'Jim'}
my_d[2] = 'Test 2'
print(my_d) """
#output:{1: 'Test', 'Name': 'Jim', 2: 'Test 2'}

#3
""" my_d = {1:'Test', 'Name': 'Jim'}
my_d[1] = 'Not a test!'
print(my_d) """
#output: {1: 'Not a test!', 'Name': 'Jim'}

#4 não permite uma chave com dois valores
""" my_d = {1:'Test', 'Name': 'Jim', 1: 'Not a test!' }
my_d[1] = 'Not a test!'
print(my_d) """
#output: {1: 'Not a test!', 'Name': 'Jim'}

#5
""" my_d = {1:'Test', 'Name': 'Jim'}

for x in my_d:
    print(x) """

#output: 1 and Name in column

#6
""" 
my_d = {1:'Test', 'Name': 'Jim'}

for key, value in my_d.items():
    print(str(key) + " : " + value) """

#output(in column): 1 : Test Name : Jim

