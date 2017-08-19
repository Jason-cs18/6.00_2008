###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

# 计算每一次的输出，6a + 9b + 20c = amounts
# 思路是先从c着手，c = 0, 1, 2, ... -> b = 0, 1, 2, ... -> c = 0, 1, 2, ...
# 三个循环
def computeDiophantine(amounts, packages):
    #print(amounts)
    idex1 = int(amounts/packages[2])
    i = 0
    while (i <= idex1):
        j = 0
        idex2 = int((amounts-packages[2]*i)/packages[1])
        while (j <= idex2):
            k = 0
            idex3 = int((amounts-packages[1]*j-packages[2]*i)/packages[0])
            while (k <= idex3):
                if (packages[0]*k+packages[1]*j+packages[2]*i == amounts):
                    return 1
                k += 1
            j += 1
        i += 1
    return 0



bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6,9,20)   # variable that contains package sizes

counter = 0
falsedList = []

for n in range(1, 150):   # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFar
    if computeDiophantine(n, packages) & computeDiophantine(n+1, packages):
        counter += 1
    else:
        counter = 0
        falsedList.append(n)
    if counter >= (packages[0]-1):
        bestSoFar = falsedList.pop()
        print('Given package sizes {0}, {1}, and {2}, the largest number of McNuggets that cannot be bought in exact quantity is: {3}'.format(packages[0], packages[1], packages[2], bestSoFar))
        break
        #print(index)
