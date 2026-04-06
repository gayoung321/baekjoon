alist=[]
a, b=map(int, input().split())
for i in range(1, b+1):
    c=a*i
    reverse_c = int(str(c)[::-1])
    alist.append(reverse_c)
alist.sort(reverse=True)
print(alist[0])
