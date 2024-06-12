def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
    cleaned_string = ''.join(input_string.split()).lower()
    
    # Compare the string to its reverse
    is_palindrome = cleaned_string == cleaned_string[::-1]
    
    # Print the result based on the comparison
    if is_palindrome:
        print(f"'{input_string}' is a palindrome.")
    else:
        print(f"'{input_string}' is not a palindrome.")

# Example usage
example_string = "Max"
is_palindrome(example_string)
