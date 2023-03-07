#1
""" with open('newfile.txt', 'w') as file:
    file.writelines(["This is a new file created!", "This is another line to be added."])
     output: This is a new file created!This is another line to be added. """

#2
""" with open('newfile.txt', 'w') as file:
    file.writelines(["This is a new file created!", "\nThis is another line to be added."]) 
    output: 
    This is a new file created!
    This is another line to be added.
    """

#3
""" with open('newfile.txt', 'a') as file:
    file.writelines(["\nThis is a new file created!", "\nThis is another line to be added."])
output: 

This is a new file created!
This is another line to be added.
This is a new file created!
This is another line to be added. """

#4
""" try:
    with open('sample/newfile.txt', 'w') as file:
        file.writelines(["\nThis is a new file created!", "\nThis is another line to be added."])
except FileNotFoundError as e:
    print("Error", e) """

