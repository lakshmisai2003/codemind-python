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
s=n+m
s=s+1
c=0
while (s>0):
    c+=1
    if(prime(s)):
        break
    s+=1
print(c)