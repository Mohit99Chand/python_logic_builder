# Given a positive integer n, we have to find the sum of squares of first n natural numbers
# Input         Output          Explaination
#   2             5               1^2+2^2
#   8             204             1^2+2^2+3^2+4^2+5^2+6^2+7^2+8^2
#   4             30              1^2+2^2+3^2+4^2


""" As of now there are 2 approaches through which this problem can be solved.
                                       Time Complexity   Space Complexity
 Approach1: using while loop               O(n)            O(1)
 Approach2: Using Mathematical formula     O(1)            O(1)
"""


# Approach1:

def sum_square(i):
    total = 0
    while(i>0):
        total += i**2
        i -= 1 
    return total

num = int(input("Enter the number whose square  you want: ")) 
print(sum_square(num)) 



# Approach2: k*(K+1)*(2*K +1)/6

def sum_square(n):
    return n*(n+1)*(2*n + 1)//6

num = int(input("Enter the number whose square  you want: ")) 
print(sum_square(num))



