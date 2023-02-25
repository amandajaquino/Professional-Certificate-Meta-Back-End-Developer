#1
""" set_a = {1, 2, 3, 4, 5}

print(set_a) """

#output:{1, 2, 3, 4, 5}

#2
""" set_a = {1, 2, 3, 4, 5, 5}

print(set_a) """

#output:{1, 2, 3, 4, 5}

#3
""" set_a = {1, 2, 3, 4, 5, 5}
set_a.add(6)

print(set_a) """

#output:{1, 2, 3, 4, 5, 6}

#4
""" set_a = {1, 2, 3, 4, 5, 5}
set_a.remove(2)

print(set_a) """

#output:{1, 3, 4, 5}


#5 (união/ou)

""" set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a.union(set_b))
 """
# output: {1, 2, 3, 4, 5, 6, 7, 8}


""" set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a | set_b) """
# output: {1, 2, 3, 4, 5, 6, 7, 8}

#6 (intersection/e)

""" set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a.intersection(set_b))  """
#output: {4, 5}

""" set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a & set_b)  """
#output: {4, 5}

#7 (difference, -, symetric_difference, ^)

""" set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a.difference(set_b))  """
#output: {1, 2, 3}

""" set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a - set_b)  """
#output: {1, 2, 3}

""" set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a.symmetric_difference(set_b))   """
#output: {1, 2, 3, 6, 7, 8}

""" set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a ^ set_b)   """
#output: {1, 2, 3, 6, 7, 8}

#7 set is not subscriptable
""" set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a[0])  """
#output: 'set' object is not subscriptable
