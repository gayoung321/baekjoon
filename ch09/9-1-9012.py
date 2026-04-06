a=int(input())
alist=[]
for _ in range(a):
    b=input()
    alist.append(b)
for i in range(len(alist)):
    c=alist[i]
    left=0
    right=0
    for j in range(len(c)):
        if left>=right:
            if c[j:j+1]=='(':
                left+=1
            else:
                right+=1
        else:
            break
    if (left==right):
        print("YES")
    else:
        print("NO")
