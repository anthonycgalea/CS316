print("LCS Program")
word1 = input("Please enter word 1:\t")
word2 = input("Please enter word 2:\t")
numMatrix = []
dirMatrix = []

for k in range(len(word2)):
    arr = []
    arr2 = []
    if k > 0:
        prevNum = numMatrix[k-1][0]
    else:
        prevNum = 0
    for l in range(len(word1)):
        max = prevNum
        dir = "L"
        if (k > 0 ):
            if (max < numMatrix[k-1][l]):
                max = numMatrix[k-1][l]
                dir = "U"
        if (l > 0):
            if (max < arr[l-1]):
                max = arr[l-1]
                dir = "L"
        if (word1[l] == word2[k]):
            if (k > 0 and l > 0):
                max = numMatrix[k-1][l-1] + 1
            else:
                max = 1
            dir = "UL"
        prevNum = max
        arr.append(max)
        arr2.append(dir)
    numMatrix.append(arr)
    dirMatrix.append(arr2)

x = len(word1) - 1
y = len(word2) - 1
LCS = ""

while(x >= 0 and y >= 0):
    if (dirMatrix[y][x] == "L"):
        x=x-1
    elif(dirMatrix[y][x] == "U"):
        y=y-1
    else:
        LCS=word1[x]+LCS
        x=x-1
        y=y-1

print("LCS is " + LCS)