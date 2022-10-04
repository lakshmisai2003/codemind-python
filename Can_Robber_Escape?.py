def escape(m):
    for i in m:
        if i>=n:
            return "NO"
    return "YES"
n=int(input())
m=list(map(int,input().split()))
print(escape(m))
