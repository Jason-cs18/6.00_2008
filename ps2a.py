 # Problem Set 2 (Part I)
 # Name: Yan Lu
 # Collaborators: None
 # Time: 13:39
 #

# 找到使这个等式不成立的最大amounts
# 6a + 9b + 20c = amounts
# 策略：先使用写好的computeDiophantine函数计算
# amounts这个数是否可以使上面的等式实现，如果不能实现, 就加入
# 失败列表里，定义一个计数器counter，记录成功的次数，如果连续6次函数返回True
# 跳出循环，输出列表中的最后一个数
def findLargest():
    index = 1
    counter = 0
    falsedList = []
    while counter < 5:
        if computeDiophantine(index) & computeDiophantine(index+1):
            counter += 1
        else:
            counter = 0
            falsedList.append(index)
        index += 1
        #print(index)
    print('Largest number of McNuggets that cannot be bought in exact quantity: ', falsedList.pop())


# 计算每一次的输出，6a + 9b + 20c = amounts
# 思路是先从c着手，c = 0, 1, 2, ... -> b = 0, 1, 2, ... -> c = 0, 1, 2, ...
# 三个循环
def computeDiophantine(amounts):
    #print(amounts)
    idex1 = int(amounts/20)
    i = 0
    while (i <= idex1):
        j = 0
        idex2 = int((amounts-20*i)/9)
        while (j <= idex2):
            k = 0
            idex3 = int((amounts-9*j-20*i)/6)
            while (k <= idex3):
                if (6*k+9*j+20*i == amounts):
                    return 1
                k += 1
            j += 1
        i += 1
    return 0
