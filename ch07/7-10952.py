a=1
b=1
alist=[]
while (a!=0 and b!=0):
    a, b=map(int, input().split())
    c=a+b
    alist.append(c)
for i in range(len(alist)-1):
    print(alist[i])
