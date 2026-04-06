a=int(input())
alist=[]
blist=[]
clist=[]
for _ in range(a):
    temp1, temp2 =map(int, input().split())
    tem=temp1+temp2
    alist.append(tem)
    blist.append(temp1)
    clist.append(temp2)


for i in range(a):
    temp=alist[i]
    temp1=blist[i]
    temp2=clist[i]

    print("Case #%d: %d + %d = %d" % (i + 1, temp1, temp2, temp))
    
