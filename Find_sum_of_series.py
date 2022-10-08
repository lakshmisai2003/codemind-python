n=int(input())
su=0
for i in range(1,n+1):
    r=1/i
    #print(r)
    su+=r
res="{:.2f}".format(su)
print(res)
    