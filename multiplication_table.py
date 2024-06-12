def print_multiplication_table():
    # Iterate through numbers 1 to 10 for rows
    for i in range(1, 11):
        # Iterate through numbers 1 to 10 for columns
        for j in range(1, 11):
            # Print the product of the current row and column number
            print(f"{i * j:4}", end=' ')
        # Print a newline after each row
        print()

# Call the function to print the multiplication table
print_multiplication_table()
