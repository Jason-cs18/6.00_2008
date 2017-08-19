# Problem Set 1
 # Name: Yan Lu
 # Collaborators: No one
 # Time: 14:50-15:13
 #

# 判断质数的函数
def isPrime(k):
    i = 2
    while(i < k):
        if (k%i) == 0:
            return False
        i += 1
    return True
# 初始化计数器与数字，以及一行的最大输出个数
index = 1
numbers = 2
count = 0
while index <= 1000:
    if isPrime(numbers):
        count += 1
        index += 1
        print(numbers, end=' ')
        if(count%10==0):
            print(end='\n')
            count = 0
    numbers += 1
