def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

n = int(input())
m = n
s=0
while n>0:
    d = n%10
    s+=fact(d)
    n = n//10
print(s==m)