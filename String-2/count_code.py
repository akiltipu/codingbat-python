# Return the number of times that the string "code" appears anywhere in the given string, 
# we'll accept any letter for the 'd', so "cope" and "cooe" count.


# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(str):
    alp = "abcdefghijklmnopqersuvwxuz"
    sum = 0
    for c in alp:
        d  = "co" + c + "e"
    
        for i in range(len(str)-1):
            if str[i:i+4] == d:
                sum += 1
                
    return sum
