def su(x):
    s=0
    for i in range(1,(x//2)+1):
        if x%i==0:
            s+=i
    return s
n=int(input())
m=int(input())
r1=su(n)
r2=su(m)
if r1==m and r2==n:
    print("Amicable")
else:
    print("Not Amicable")