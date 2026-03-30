n=int(input())
a=n%4
b=n%100
c=n%400
if (a==0):
    if(b!=0):
        print('1')
    elif(c==0):
        print('1')
    else:
        print('0')
else:
    print('0')
