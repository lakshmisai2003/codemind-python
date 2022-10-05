num1,num2=map(int,input().split())
if num2>num1
    big=num2 
else:
    big=num1
a=big 
k=2
while True:
    if big%num1==0 and big%num2==0:
        lcm=big
        print(lcm)
        break
    else:
        big=a*k
        k+=1