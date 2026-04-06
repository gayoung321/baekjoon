alist=[]
for _ in range(10):
    a=int(input())
    b=a%42
    alist.append(b)
k=set(alist)
print(len(k))
