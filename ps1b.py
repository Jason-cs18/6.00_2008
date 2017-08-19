# Problem Set 1
 # Name: Yan Lu
 # Collaborators: No one
 # Time: 15:20-15:29
 #
from math import *
# 判断质数的函数
def isPrime(k):
    i = 2
    while(i < k):
        if (k%i) == 0:
            return False
        i += 1
    return True
# 输出从2到n之间所有prime的乘积
def productPrime(n):
    # 初始化计数器与数字，以及一行的最大输出个数, 乘积
    index = 1
    numbers = 2
    product = 1
    while index <= n:
        if isPrime(numbers):
            index += 1
            product *= numbers
        numbers += 1
    print(log(product))
# 输出
n = input('Enter a number: ')
productPrime(int(n))
