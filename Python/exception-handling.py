#1 - without error
""" def divide_by(a,b):
    return a/b
print(divide_by(40, 4)) """

#2
""" def divide_by(a,b):
    return a/b
try:
    print(divide_by(40, 0))
except:
    print("Something went wrong!")
output: Something went wrong """

#3 -class
""" def divide_by(a,b):
    return a/b
try:
    ans = divide_by(40, 4)
except:
    print("Something went wrong!")
#output: nothing appear in output and terminal """

#4
""" def divide_by(a,b):
    return a/b
try:
    print(divide_by(40, 0))
except Exception as e:
    print("Something went wrong!", e) 
#output: Something went wrong! division by zero
"""

#5
""" def divide_by(a,b):
    return a/b
try:
    print(divide_by(40, 0))
except Exception as e:
    print("Something went wrong!", e) 
    print(e.__class__) 
#output: Something went wrong! division by zero
<class 'ZeroDivisionError'> 
"""

#6
""" def divide_by(a,b):
    return a/b
try:
    print(divide_by(40, 0))
except ZeroDivisionError as e:
    print(e, "Something went wrong!")
#output:  division by zero Something went wrong!     
  """

#7
""" def divide_by(a,b):
    return a/b
try:
    print(divide_by(40, 0))
except ZeroDivisionError as e:
    print(e, "Something went wrong!")
except Exception as e:
    print(e, "Something went wrong!") """
#output: division by zero Something went wrong!