def even_odd_checker():
    try:
        # Initialize an input to allow dynamic user input
        num = int(input("Enter any number"));

        # Check if num is diisible by 2
        if num % 2 == 0:
            # If num is divisible by 2 print its even
            print(f"{num} is an even number");
        else:
            # If num is not divisible by 2 print its odd
            print((f"{num} is an odd number"));
    except ValueError:
        # If user enters an input that is not an int
        print("Input must be an integer");


# Call the method
even_odd_checker()