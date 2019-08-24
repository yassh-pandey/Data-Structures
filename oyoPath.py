globalPathSumList = []
counter = 0
def traverse(arr, currentPosition=None, pathSum=None):
    print(currentPosition)
    global counter
    counter+=1
    if currentPosition==None:
        currentPosition=(0, 0)
    if pathSum==None:
        pathSum=0
    if currentPosition==(len(arr)-1, len(arr[0]) -1):
        pathSum += arr[currentPosition[0]][currentPosition[1]]
        globalPathSumList.append(pathSum)
        return 
    pathSum += arr[currentPosition[0]][currentPosition[1]]
    if currentPosition[0]+1 < len(arr):
        traverse(arr, (currentPosition[0]+1, currentPosition[1]), pathSum)
    if currentPosition[1]+1 < len(arr[0]):
        traverse(arr, (currentPosition[0], currentPosition[1]+1), pathSum)

traverse([[1, 3, 2], [4, 3, 1], [5, 6, 1], [1, 1, 1]])
print(min(globalPathSumList))
print(counter)