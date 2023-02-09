#1

""" num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for item in num_list:
        print (item)  """

#2

""" num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for item in num_list:
    if item > 45:
        print (item) """

#3

""" num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]


for num in num_list:
    if num > 45:
        print('Over 45')
    else:
        print('Under 45') """



#4
""" num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for x,num in enumerate(num_list):
    if num == 36:
        print('Number found at ', x) """

#5, 6 and 7

""" num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)
        break

print(count) """



#others
""" num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

num_list.sort()
print (num_list) """

""" num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
temp = 0

for i in range(0, len(num_list)):    
    for j in range(i+1, len(num_list)):    
        if(num_list[i] > num_list[j]):    
            temp = num_list[i];    
            num_list[i] = num_list[j];    
            num_list[j] = temp;   

print(num_list)  """



