a=int(input())
alist=[]

for _ in range(a):
    temp1, temp2 =map(int, input().split())
    tem=temp1+temp2
    alist.append(tem)

for i in range(a):
    temp=alist[i]
    print(temp)
