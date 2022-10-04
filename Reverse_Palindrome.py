def pal(n):
    rev=0
    temp=n
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if(rev==temp):
        return True
    return False
def rev(n):
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
r=rev(n)
s=n+r
while(s>0):
    if pal(s):
        print(s)
        break
    else:
        s=s+rev(s)