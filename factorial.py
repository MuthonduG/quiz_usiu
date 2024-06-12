def factorial(n):
    # Check if the input is a positive integer
    if n < 0:
        raise ValueError("Input must be a positive integer.")
    
    # Initialize the factorial result to 1
    result = 1
    
    # Use a for loop to calculate the factorial
    for i in range(1, n + 1):
        result *= i  # Corrected operator to multiplication
    
    print(result)

factorial(9)