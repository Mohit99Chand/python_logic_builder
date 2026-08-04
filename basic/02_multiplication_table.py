"""
This program demonstrates the difference between iterative and recursive approaches.

It first implements:
1. Multiplication Table
2. Printing numbers from n to 0

using the iterative approach, and then solves the same problems using recursion.
 """
#1. Multiplication Table
#iterative approach
class Multiplicator:
    def mul(self, n):
        
        for x in range(1,11):
            print(f'{n} * {x} = {n*x}')

if __name__ == "__main__":
    n = int(input("Enter the number whoes multiplication table is needed: "))
    print(f"Multiplication table of {n}")
    
    obj = Multiplicator() 
    obj.mul(n)


#Recursive approach
class Multiplicator:
    def mul(self, n):
        
        x +=1
        print(f'{n} * {x} = {n*x}')
        obj.mul(n)

if __name__ == "__main__":
    n = int(input("Enter the number whoes multiplication table is needed: "))
    print(f"Multiplication table of {n}")
    
    obj = Multiplicator() 
    obj.mul(n)