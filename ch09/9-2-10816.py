a=int(input())
alist=list(map(int, input().split()))
dicta={}
for num in alist:
    if num in dicta:
        dicta[num]+=1
    else:
        dicta[num]=1
b=int(input())
blist=list(map(int, input().split()))
for i in range(b):
    if blist[i] in dicta:
        final = dicta.get(blist[i])
        print(final, end=' ')
    else:
        final='0'
        print(final, end=' ')
