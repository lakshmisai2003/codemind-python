from math import sqrt
def prime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
m=int(input())
for i in range(n,m):
    if prime(i):
        print(i)