word=' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
a=input()
alist=[]
blist=[]
sum=0
for i in range(len(a)):
    k=a[i:i+1]
    alist.append(k)
    for j in range(len(word)):
        m=word[j:j+1]
        if (m==alist[i]):
            blist.append(j)
            break
for n in range(len(blist)):
    sum+= blist[n]

c=0
if sum<2:
    c=0
for i in range(2, int(sum**0.5)+1):
    if sum%i == 0:
        c=1

if c==0:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
