# Given an int array length 2, 
# return True if it contains a 2 or a 3.


# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

def has23(nums):
    return 2 == nums[0] or 2 == nums[1] or 3 == nums[0] or 3 == nums[1]
