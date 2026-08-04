# Given a positive integer n, find sum of first n natural no.
# input           output            Explaination
#  3                6                 1+2+3
#  5                15                1+2+3+4+5

# Sloving method
# Method1: using loop
# Method2: using recursion
# Method3: Using formula 

# Method1: Using for loop 
def sum_natural(n):
    sum = 0
    for i in range(1,n+1):
        sum +=i
    return sum

n = int(input("Enter the natural number whose sum you want: "))
print(sum_natural(n))  
    

#Method2: using recursion 

def sum_natural(number):
    if number == 1:
        return 1
    return number + sum_natural(number-1)

number = int(input("Enter the natural number whose sum you want:"))
print(sum_natural(number)) 



#Method3: formula based [(n*(n+1))/2]
def sum_natural(n):
    return (n*(n+1))//2

number = int(input("Enter the natural number whose sum you want:"))
print(sum_natural(number))



