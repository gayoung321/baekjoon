a=int(input())
b=0
while a>=0:
    if (a%5==0):
        b=b+(a//5)
        print(b)
        break
    a=a-3
    b=b+1
else:
    print(-1)
