a=int(input())
klist=[]
for _ in range(a):
    k=input()
    klist.append(k)
for i in range(len(klist)):
    m=klist[i]
    sum=0
    count=0
    for j in range(len(m)):
        if m[j:j+1]=='O':
            count+=1
            sum+=count
        else:
            count=0
    print(sum)
