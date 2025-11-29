n = int(input())
l = []
s = 999999999
while s>9:
    while n>0:
        d = n%10
        l.append(d)
        n = n//10
    s = sum(l)
    l=[]
    n=s
print(s)