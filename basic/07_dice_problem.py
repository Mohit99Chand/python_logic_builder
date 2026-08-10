# You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. 
# The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face 
# of this cube, your task is to guess the number on the opposite face of the cube.


""" 
 There ared two approach to solve this problem:
 Approach1: If-else just like switch case
 Approach2: Total sum of opposite side is 7. Reducing the known value will result the unknown side.
"""

# Approach 1: 

def result(n):
    if n == 1:
        return 6
    elif n == 2:
        return 5
    elif n == 3:
        return 4
    elif n == 4:
        return 3
    elif n == 5:
        return 2
    else:
        return 1

value = int(input("Enter the face value whose opposite side you want:  "))
print(result(value))



# Approach2:

def result(n):
    return 7-n


value = int(input("Enter the face value whose opposite side you want:  "))
print(result(value))

