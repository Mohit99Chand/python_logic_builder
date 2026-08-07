# Given two integers n and m (m != 0). Find the number closest to n and divisible by m. 
# If there is more than one such number, then output the one having maximum absolute value.

# input(n,m)        Output          
#   13,4              12
#  -15,6             -18 

# Requirement: number 
# codition: number divisible by m
#       	number closest to n
#	        number should be maximum absolute value


def closest_divisible(n: int, m: int) -> int:
    if m == 0:
        raise ValueError("m must not be zero.")
    m = abs(m) 
    q = int(n / m)
    candidate1 = q * m
    candidate2 = q * m + m if n >= 0 else q * m - m
    dist1 = abs(n - candidate1)
    dist2 = abs(n - candidate2)
    if dist1 < dist2:
        return candidate1
    elif dist2 < dist1:
        return candidate2
    else:
        return candidate1 if abs(candidate1) >= abs(candidate2) else candidate2

if __name__ == "__main__":
    
        n = int(input("\nEnter n : "))
        m = int(input("Enter m : "))
        result = closest_divisible(n, m)
        print(f"\nClosest number to {n} divisible by {m}:  {result}")
    
 