a=int(input())
alist=set(map(int, input().split()))
b=int(input())
blist=list(map(int, input().split()))
for i in range(len(blist)):
    if blist[i] in alist:
        print(1, end=' ')
    else:
        print(0, end=' ')
