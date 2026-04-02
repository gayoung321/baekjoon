a=int(input())
blist=[]
suma=0
count=0
for i in range(a):
    suma=0
    count=0
    blist=list(map(int, input().split()))
    for j in range(1, len(blist)):
        suma+=blist[j]
    eval=suma/blist[0]
    for j in range(1, len(blist)):
        if blist[j]>eval:
            count+=1
    k=(count/blist[0])*100
    print(f"{k:.3f}%")
