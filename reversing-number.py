#Reversing a number
n = int(input())
l = len(str(n))
rev = 0
while n>0:
    d = n%10
    rev = d*10**(l-1) + rev
    n = n//10
    l=l-1
print(rev)
