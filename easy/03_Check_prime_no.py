# Given a number n, check whether it is a prime number or not.
# Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.


"""
There are three ways to solve this problem:
Approach1:  Basic trial division
Approach2: Square root trial division
Approach3: Optimized square root trail division
"""

#Approach 1: Basic trial division
def check_prime(n):
    if (n==2 or n==3 or n==5):
        return f"{n} is a prime no"
    elif ((n <= 0) or (n%2 == 0) or (n%3 == 0) or (n%5 == 0)):
        return f"{n} is not a prime no"
    else:
        return f"{n} is a prime no"

if __name__ == "__main__":
    num = int(input("Enter the value: "))
    print(check_prime(num))

