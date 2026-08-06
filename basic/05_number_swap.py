# Given two numbers, the task is to swap them
# Input(a,b)           Output(a,b)     
#  4,5                   5,4
# 20,0                   0,20
# 10,10                 10,10



"""There are 4 approaches to solve this problem.
    Approach1: using third variable
    Approach2: using simple python object referencing concept
    Approach3: using mathematical operation
    Approach3: using Bitwise XOR
    Approach3: using built in swap method  """


# Approach 1:
def exchange(a,b):
    temp = 0
    temp = a
    a = b
    b=temp
    return a,b

first = int(input("Enter the first number: "))
secnd = int(input("Enter the second number: "))
print(f'The first and second number after swapping are {exchange(first, secnd)}')
    

# Approach 2: 
def exchange(a,b):
    a,b = b,a
    return a,b

first = int(input("Enter the first number: "))
secnd = int(input("Enter the second number: "))
print(f'The first and second number after swapping are {exchange(first, secnd)}')



# Approach 3:
def exchange(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b

first = int(input("Enter the first number: "))
secnd = int(input("Enter the second number: "))
print(f'The first and second number after swapping are {exchange(first, secnd)}')


# Approach 4:
def exchange(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a,b

first = int(input("Enter the first number: "))
secnd = int(input("Enter the second number: "))
print(f'The first and second number after swapping are {exchange(first, secnd)}')



# Approach 5:
def swap(a,b):
    return b,a

first = int(input("Enter the first number: "))
secnd = int(input("Enter the second number: "))
print(f'The first and second number after swapping are {swap(first, secnd)}')
