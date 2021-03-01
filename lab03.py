def multiply(x,y):
    if x == 0 or y == 0:
        return 0
    if y == 1:
        return x
    if x == 1:
        return y
    else:
        return(x + multiply(x, y-1))

def collectOddValues(listOfInt):
    if len(listOfInt) == 0:
        return []
    if listOfInt[0] % 2 == 1:
        return [listOfInt[0]] + collectOddValues(listOfInt[1:])
    else:
        return collectOddValues(listOfInt[1:])

def countInts(listOfInt, num):
    if len(listOfInt) == 0:
        return 0
    if len(listOfInt) == 1:
        if num == listOfInt[0]:
            return 1
        else: 
            return 0
    elif num == listOfInt[0]:
        return 1 + countInts(listOfInt[1:], num)
    else:
        return countInts(listOfInt[1:], num)

def reverseString(s):
    if s == "" or len(s) == 1:
        return s
    else:
        return s[-1] + reverseString(s[:-1])

def removeSubString(s, sub):
    if sub not in s:
        return s
    else:
        return s[:s.find(sub)] + removeSubString(s[(s.find(sub) + len(sub)):], sub)

