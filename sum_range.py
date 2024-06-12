def sum_in_range():
    try:
        # Initialize an input to allow dynamic user input
        num = int(input("Enter any number: "))
        
        # Initialize a variable with value of 0
        n, total_sum = 0, 0
        
        # Use while loop for addition
        while n < num:
            n += 1
            total_sum += n
        
        print(total_sum)
    except ValueError:
        # If user enters an input that is not an int
        print("Input must be an integer")

# Call the method
sum_in_range()