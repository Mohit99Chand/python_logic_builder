#Given an Integer n, find the reverse of its digits.
# Input         Output          
#  122            221
#  200            2
# 12345           54321

"""
There are three approaches to this problem-
Approach1: Reversing digit by digit - we move forward by storing remainder value obtained by dividing the number with 10.
Approach2: Using list and reverse function 
Approach3: Using String slicing

"""

# Approach1:
"""
def rev_num(num):
    remind, rev_value = 0,0
    while(num != 0):
        remind = num % 10
        num = num // 10
        rev_value = rev_value*10 + remind 

    return rev_value


if __name__ == "__main__":
    n = int(input("Enetr the no: "))
    print(rev_num(n))
"""

#Approach 2:
"""
def rev_num(value):
    value.reverse()
    return ''.join(value)

if __name__ == "__main__":
    value = list(input("Enter the number: "))
    print(rev_num(value))
"""

#Approach 3:
def rev_num(val):
    return val[::-1]

if __name__ == "__main__":
    value = input("Enter the number: ")
    print(rev_num(value))




