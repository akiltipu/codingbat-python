# Given an array of ints, 
# return the sum of the first 2 elements in the array. 
# If the array length is less than 2, 
# just sum up the elements that exist, 
# returning 0 if the array is length 0.


# sum2([1, 2, 3]) → 3
# sum2([1, 1]) → 2
# sum2([1, 1, 1, 1]) → 2

def sum2(nums):
    if len(nums) < 2:
        return sum(nums)
    else:
        return nums[0]+nums[1]
