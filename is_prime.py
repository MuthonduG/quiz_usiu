import math

def is_prime(n):
    # Return False for numbers less than 2
    if n <= 1:
        print(f"{n} is not a prime number.")
        return False
    
    # Check divisibility from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            return False
    
    print(f"{n} is a prime number.")
    return True

# Example usage
number = 3
is_prime(number)
