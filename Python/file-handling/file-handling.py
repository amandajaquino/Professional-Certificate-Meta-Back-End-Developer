""" import os
# Get the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# List the files in the current directory
files = os.listdir(cwd)
print("Files in current directory:", files)

# Change the current working directory
os.chdir('C:/Users/aquin/OneDrive/2022/Projects/Software Engineer/Courses/Coursera/Back-end by meta/Activities/Python/file-handling')

# Get the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# List the files in the current directory
files = os.listdir(cwd)
print("Files in current directory:", files) """


#1
""" file = open('test.txt', mode = 'r')

data = file.readline()

print(data)

file.close() """

with open('test.txt', mode = 'r') as file:
    data = file.readline()

    print(data)



