from math import sqrt
def isprime(n):
    if n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if (not(isprime(i))):
            c+=1
print(c)