def fac(n):
    fc=1
    while(n>0):
        fc=fc*n
        n-=1
    return fc
n=int(input())
temp=n
s=0
while(n>0):
    r=n%10
    s+=fac(r)
    n=n//10
if(s==temp):
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")