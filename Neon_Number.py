def su(n):
    s=0
    while(n>0):
        r=n%10
        s+=r
        n=n//10
    return s
n=int(input())
sq=n**2
res=su(sq)
if res==n:
    print("Neon Number")
else:
    print("Not Neon Number")