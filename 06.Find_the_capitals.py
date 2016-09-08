def capitals(word):
    #your code here
    result = []
    for i, w in enumerate(word):
        if w.isupper():
            result.append(i)
            
    return result

# Another Solution

def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]
