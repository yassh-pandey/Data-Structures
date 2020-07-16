#Given an input string we need to compute the next String sequence that is greater than it by rearranging the input string characters.
#This difference b/w the two strings should be minimum.
#A string is greater than other string if it comes after it in a dictionary (lexicographical order)

def nextDictSeq(inputStr):
	#Input string in lower case (if there is any capital letter present)
	inputStrL = inputStr.lower()
	reverseStrL = inputStrL[::-1]

	#If all the characters are same then return the same string
	allCharactersSame = True
	for index, char in enumerate(inputStrL):
		if char != inputStrL[0]:
			allCharactersSame = False
			break
	if allCharactersSame:
		return inputStrL

	#Special boundary case when the input string is of length two
	if len(inputStrL)==2 and inputStrL[1] > inputStrL[0]:
		return inputStrL[::-1]
	elif len(inputStrL)==2 and inputStrL[1] < inputStrL[0]:
		return inputStrL

	#Other general case
	done = False
	for outerIndex, outerChar in enumerate(reverseStrL):
		if outerIndex == len(reverseStrL)-1:
			continue
		else:
			for innerIndex, innerChar in enumerate(reverseStrL):
				#Reverse the string and find the character from back that is just bigger than our current element
				if(innerIndex!=outerIndex and innerIndex>outerIndex and innerIndex!=len(reverseStrL)-1):
					if outerChar > innerChar:
						done = True
						#Appropriate string manipulation to make string of the form we need
						dummyList = list(reverseStrL)
						temp = innerChar
						dummyList[innerIndex] = outerChar
						dummyList[outerIndex] = temp
						stringAfterReplace = "".join(dummyList)
						firstPart = "".join(sorted(stringAfterReplace[:innerIndex]))
						secondPart = stringAfterReplace[innerIndex:][::-1]
						resultString = secondPart + firstPart
						return resultString
	if done==False:
		#We are unable to find the next greatest subsequence without changing the MSB of the input string (first character)
		frontlineCharacter=""
		for ch in sorted(inputStrL):
			if ch > inputStrL[0]:
				#Found character JUST greater than our first character of the original input string
				#This will be the first character of the new string
				#The rest of the characters will be remaining characters sorted in ascending order
				frontlineCharacter = ch
				done=True
				break;
		if done:
			newList = list(inputStrL[:])
			newList.remove(frontlineCharacter)
			return frontlineCharacter+"".join(sorted(newList))
		else:
			return inputStrL


result = nextDictSeq("abaaagtedddd")
print(result)
