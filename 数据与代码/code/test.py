import math
import numpy as np

def test(n):
    product = np.zeros(n+1)
    if n<2:
        return 0
    if n==2:
        return 1
    if n==3:
        return 2
    product[0] = 0
    product[1] = 1
    product[2] = 2
    product[3] = 3

    for i in range(4,n+1):

        max_num = 0
        for j in range(0, math.floor(i/2)+1):
            num = product[j]*product[i-j]
            if max_num<num:
                max_num = num
                product[i]=max_num
    max_num = product[n]
    return max_num

if __name__ == '__main__':
    a = test(20)
    print(a)