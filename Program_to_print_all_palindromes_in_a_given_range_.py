def pal(n):
    rev=0
    temp=n
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==temp:
        return True
    return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if pal(i):
        print(i,end=" ")