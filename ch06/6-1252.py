a, b=input().split()
alist=list(a)
blist=list(b)
diff=(len(alist)-len(blist))
if (diff>=0):
    for _ in range(abs(diff)):
        b="0"+b
else:
    for _ in range(abs(diff)):
        a="0"+a
        
a=int(a, 2)
b=int(b, 2)
c=a+b
c=bin(c)
print(c[2:])
