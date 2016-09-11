# Mumbling
# 
# This time no story, no theory. The examples below show you how to write function accum:
# 
# accum("abcd")    # "A-Bb-Ccc-Dddd"
# accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt")    # "C-Ww-Aaa-Tttt"
#

def accum(s):
    # your code
    result = []
    for i, w in enumerate(s):
        tmp = ""
        for x in range(i+1):
            tmp += w.upper() if x == 0 else w.lower()
        result.append(tmp)
        
    return '-'.join(result)

accum(test)
