alist=[]
for _ in range(9):
    a=int(input())
    alist.append(a)
m=max(alist)
for i in range(len(alist)):
    if alist[i]==m:
        break

print(m)
print(i+1)
