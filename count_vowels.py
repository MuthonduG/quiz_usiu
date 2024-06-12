def count_vowels(input_string):
    # Define a set of vowels
    vowels = set("aeiouAEIOU")
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Iterate through each character in the string
    for char in input_string:
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1
    
    print(vowel_count)

# Example usage
example_string = "Hello, World!"

# call the method
count_vowels(example_string)