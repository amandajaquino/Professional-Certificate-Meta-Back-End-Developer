#1
""" def sum_of(a, b):
    return a + b

print(sum_of(4, 5)) """
#output: 9

#2
""" def sum_of(a, b):
    return a + b

print(sum_of(4, 5, 6)) """

#output: error TypeError: sum_of() takes 2 positional arguments but 3 were given

#3
""" def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(4, 5, 6)) """

#output: 15

""" def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(4, 5, 6, 4, 5, 6)) """

#output: 30

""" def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return sum

print(sum_of(coffee=2.99, cake=4.55, juice=2.99))
 """
#output: 10.530000000000001

""" def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)

print(sum_of(coffee=2.99, cake=4.55, juice=2.99))
 """
#output: 10.53