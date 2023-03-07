
#1
""" with open('sample.txt', 'r') as file:
    print(file.read())
output: all text """

#2

""" with open('sample.txt', 'r') as file:
    print(file.read(44))
output: the first 44 caracter """

#3
""" with open('sample.txt', 'r') as file:
    print(file.readline())
output: the first line """

#4
""" with open('sample.txt', 'r') as file:
    print(file.readlines())
output: all text """

#5
""" with open('sample.txt', 'r') as file:
    data = file.readlines()

    for x in data:
        print(x)

output: all text separate the paragraphy by line """

""" with open('sample.txt', 'r') as file:
    for x in file:
        print(x)
output: all text separate the paragraphy by line """

