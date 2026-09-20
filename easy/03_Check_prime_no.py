# Given a number n, check whether it is a prime number or not.
# Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.


"""
There are three ways to solve this problem:
Approach1:  Basic trial division
Approach2: Square root trial division
Approach3: Optimized square root trail division
"""

#Approach 1: Basic trial division
"""
def check_prime(n):
    if (n==2 or n==3 or n==5):
        return f"{n} is a prime no"
    elif ((n <= 0) or (n == 1) or (n%2 == 0) or (n%3 == 0) or (n%5 == 0)):
        return f"{n} is not a prime no"
    else:
        return f"{n} is a prime no"

if __name__ == "__main__":
    num = int(input("Enter the value: "))
    print(check_prime(num))
"""
#Approach 2: square root trial division
"""
 Trial division is a fundamental algorithm in number theory used to determine
 if a number is prime or to factorize it by testing divisibility against smaller integers.
 Working principle: If a number n has a factor, at least one of its 
 factors must be less than or equal to the square root of n(root n)
 """

def check_prime(num):
    if num < 2:
        return f"{num} is not prime"
    root = int(num ** 0.5)
    for i in range(2, root + 1):
        if num % i == 0:
            return f"{num} is not prime no"
            
    return f"{num} is prime no"

if __name__ == "__main__":
    num = int(input("Enter the number: "))
    print(check_prime(num))



#Approach 3: Optimized square root trial division
"""Optimized square root trial division is an integer factorization and primality testing
 algorithm that determines if a number is prime or finds its factors by testing divisibility 
 only up to the square root of the number, rather than the number itself.   
 Working principle: Any composite number must have at least one prime factor less than or equal
 to its square root, significantly reducing the number of required divisions."""

