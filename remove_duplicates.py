def remove_duplicates(input_list):
    # Initialize an empty list to store unique elements
    unique_list = []
    
    # Iterate through the input list
    for item in input_list:
        # Add the item to unique_list if it's not already present
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

# Example usage
original_list = [1, 2, 3, 4, 3, 2, 1, 5]
unique_list = remove_duplicates(original_list)
print("Original List:", original_list)
print("List with Duplicates Removed:", unique_list)
