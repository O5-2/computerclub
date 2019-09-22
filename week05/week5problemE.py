from sys import stdin
from math import sqrt
n = int(stdin.readline())

def divisors(num):
    if num == 1:
        return [1]
    divs = [1]
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0:
            while num%i == 0:
                divs.append(divs[-1]*i)
                num /= i
            break
    if divs == [1]:
        return [1, num]
    ans = []
    for i in divs:
        ans += [i*j for j in divisors(num)]
    return ans

print(len(divisors(n))-1)
