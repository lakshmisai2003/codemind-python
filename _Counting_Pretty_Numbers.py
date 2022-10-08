t=int(input())
for i in range(t):
    l,m=map(int,input().split())
    c=0
    for i in range(l,m+1):
        r=i%10
        if r==2 or r==3 or r==9:
            c+=1
    print(c)
            
        