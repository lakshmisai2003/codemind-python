def su(n):
    s=0
    while(n>0):
        r=n%10
        s+=r
        n=n//10
    return s
def pro(n):
    p=1
    while(n>0):
        r=n%10
        p=p*r
        n=n//10
    return p
n=int(input())
s=su(n)
p=pro(n)
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")