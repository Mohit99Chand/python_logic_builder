
"""
Problem : Check Even or odd
Given an integer n, determine whether it is even or odd.
Approach: Use the modulus operator(%) to check divisibility by 2
method1: if-else statement
method2: singke statement
"""

class Solution:
    def isEven(self, n):
        """
        Checks whether a given number is even or odd.
        Parametes:
            n (int): The number to check.
        Returns:
            bool: True if n is even, False if n is odd.
        """
        if n%2 == 0:
            return True
        else:
            return False
        #return n%2 == 0       or    n%2 != 0         #method2
obj = Solution()    
#print(obj.isEven(10))

# we can try to add user defined value via use of input()
print(obj.isEven(int(input("Enter the value to check against: "))))
