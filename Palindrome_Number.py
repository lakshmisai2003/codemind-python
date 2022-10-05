def palindrome(n):
    temp=n
    rev=0
    while(n>0):
        r=n%10
        n=n//10
        rev=rev*10+r
    if rev==temp:
        return True
    return False
t=int(input())
for i in range(t):
    n=int(input())
    res =palindrome(n)
    print(res)