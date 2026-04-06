a=int(input())
alist=[]
for i in range(a):
    b=int(input())
    if b==0:
        alist.pop()
    else:
        alist.append(b)

print(sum(alist))
