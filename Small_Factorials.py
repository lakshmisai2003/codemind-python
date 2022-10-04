def fac(n):
    fc=1
    while(n>0):
        fc=fc*n
        n-=1
    return fc
t=int(input())
for i in range(t):
    n=int(input())
    print(fac(n))