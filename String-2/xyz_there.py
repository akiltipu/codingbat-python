# Return True if the given string contains an appearance of "xyz" 
# where the xyz is not directly preceeded by a period (.). 
# So "xxyz" counts but "x.xyz" does not.


# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
    if str.startswith('xyz'):
        return True
    
    for i in range (len(str)):
        if str[i-1] != '.' and str[i:i+3] == 'xyz':
        return True
    return False