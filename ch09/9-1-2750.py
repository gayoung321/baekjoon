a=int(input())
alist=[]
for _ in range(a):
    b=int(input())
    alist.append(b)

k=set(alist)
klist=list(k)
klist.sort()
for i in klist:
    print(i)
