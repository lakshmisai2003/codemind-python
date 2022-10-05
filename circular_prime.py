from math import sqrt
def prime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
def rev(n):
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
if prime(n):
    if prime(rev(n)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
        