from math import sqrt
def square(n):
    temp=sqrt(n)
    sq=int(sqrt(n))
    if (temp-sq)==0:
        return True
    return False
t=int(input())
for i in range(t):
    n=int(input())
    print(square(n))