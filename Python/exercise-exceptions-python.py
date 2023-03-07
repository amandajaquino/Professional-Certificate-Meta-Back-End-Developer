#1
""" items = [1,2,3,4,5]   
try:
    item = items[6]
except:
    print("Item does not exist in the list")
#output: Item does not exist in the list """

#2
""" def divide_by(a, b):
    return a / b
try:
    ans = divide_by(40, 0)
except:
    print(0) """
#output: 0

#3
""" try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except Exception as e:
    print("The file could not be found", e) """
#output: The file could not be found [Errno 2] No such file or directory: 'file_does_not_exist.txt'

#4

""" try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("The file could not be found") """
#output: The file could not be found