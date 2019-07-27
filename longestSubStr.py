#Longest sub string without repetition
def lss(mainStr):
    if len(mainStr): 
        maxLength = 1
    else:
        maxLength = 0
    previous = []
    for position, char in enumerate(mainStr):
        previous.append(char)
        for char in mainStr[position+1:]:
            if char in previous:
                    previous = []
                    break
            else:
                previous.append(char)
                if len(previous) > maxLength:
                    maxLength = len(previous)
    return maxLength

print(lss("aaaaaaaxa"))
