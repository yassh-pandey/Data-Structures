def lss(mainStr):
    maxLength = 1
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