a, b=map(int, input().split())
alist=[]
blist=[]
alist=list(map(int, input().split()))
for i in alist:
    if i<b:
        blist.append(i)
    else:
        continue
print(" ".join(map(str, blist)))
