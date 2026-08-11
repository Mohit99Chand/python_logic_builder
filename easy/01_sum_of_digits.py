# Given a number n, find the sum of its digits.
#  Input       Output      Explaination
#   687         21           6+8+7
#   12          3            1+2


"""
There are 3 approaches to solve this problem:           Time complexity     Space complexity
Approach1: Using Digit Extraction                           O(Log10n)           O(1)
Approach2: Using recursion                                  O(Log10n)           O(Log10n)
Approach3: using string conversion                          O(Log10n)           O(Log10n)
"""

# Approach1:
def sumOfDigits(n):
    sum = 0
    while n != 0:
        last = n % 10
        sum += last 
        n //= 10
    return sum

if __name__ == "__main__":
	n = insert(input("Enter the number " ))
	print(sumOfDigits(n))



# Approach2:

def sumOfDigits(n):
 
    if n == 0:
        return 0
    return n % 10 + sumOfDigits(n // 10)

if __name__ == "__main__":
    num = int(insert("Enter the no"))
    print(sumOfDigits(num))



# Approach3:
def sumOfDigits(n):
     s = str(n)
    sum = 0
    for ch in s:
        sum += int(ch)

    return sum

num = int(input("Enter the number "))
print(sumOfDigits(num))