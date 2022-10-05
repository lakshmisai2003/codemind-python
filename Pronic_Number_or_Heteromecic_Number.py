def pronic(n):
    for i in range(1,int(n/2)):
        res=i*(i+1)
        if res==n:
            return "YES"
    return "NO"
n=int(input())
print(pronic(n))