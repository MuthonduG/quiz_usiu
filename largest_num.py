def is_largest(nums):
    # check the length of the list
    n = len(nums)

    # sort the list of numbers using sort
    nums.sort()

    # print the last num as it is the largest
    print(nums[n-1])

# initialize a list of numbers
nums = [90, 45, 67, 8, 10]

# Call the method
is_largest(nums)
