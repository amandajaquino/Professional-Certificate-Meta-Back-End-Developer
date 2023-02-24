# 1 global scope
""" my_global = 10

def fn1():
    local_v = 5
    print('Access to Global', my_global)
# the code before will print nothing, and it add print bellow does not work.
# print('Cant access local', local_v) // does not work
 """

#2

""" my_global = 10

def fn1():

    enclose_v = 8

    def fn2():
        local_v = 5
        print('Access to Global', my_global)
        print('Access to enclosed', enclose_v)
        print('Access to local', local_v)
    fn2()

fn1() """

#3

""" my_global = 10

def fn1():

    enclose_v = 8

    def fn2():
        local_v = 5
        print('Access to Global', my_global)
        print('Access to enclosed', enclose_v)
    fn2()

fn1()

print(enclose_v)
print(local_v) """

# error: NameError: name 'enclose_v' is not defined

