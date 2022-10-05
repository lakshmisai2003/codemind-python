def rev(n):
    rev=0
    while(n>0):
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
n=int(input())
m=abs(n)
res=rev(m)
if n<0:
    print(-1*res)
else:
    print(res)