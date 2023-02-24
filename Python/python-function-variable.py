#1 Local scope
""" def get_total(a, b):
    #local variable declared inside a function
    total = a + b
    return total
 
print(get_total(5, 2)) """

# Accessing variable outside of the function:

""" print(total) """

# with print befor NameError: name 'total' is not defined

#2 Enclosing scope

""" def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b
 
    def double_it():
        #local variable
        double = total * 2
        print(double)
 
    double_it()
    #double variable will not be accessible
    print(double)
 
    return total """
# print nothing

#3 global scope

""" def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)
 
    def double_it():
        #local variable
        double = total * 2
        print(special)
 
    double_it()
 
    return total """

#4 build-in scope

# Built-in scope refers to the reserved keywords that Python uses for its built-in functions, such as print, def, for, in, and so forth. Functions with built-in scope can be accessed at any level
