a=int(input())
for i in range(a, 1, -1):
    b=2*i-1
    temp=int((2*a-b-1)/2)
    print(' '*temp + '*'*b)
for j in range(1,a+1):
    c=2*j-1
    temp2=int((2*a-c-1)/2)
    print(' '*temp2 + '*'*c)
