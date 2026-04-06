a=int(input())
alist=list(map(int, input().split()))
alist.sort()
sumi=0
for i in range(a): 
    n=alist[i]
    sumi+=n*(i)-n*(a-1-i)
print(2*sumi)
