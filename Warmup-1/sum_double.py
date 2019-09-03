# Given two int values, return their sum.
# Unless the two values are the same, then return double their sum.


# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(a, b):
    if a == b:
        return (a+b)*2
    else:
        return a+b


# Official Solution:
# def sum_double(a, b):
#   # Store the sum in a local variable
#   sum = a + b
  
#   # Double it if a and b are the same
#   if a == b:
#     sum = sum * 2
#   return sum