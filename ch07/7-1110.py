a1=int(input())
a2=a1
cycle=0
n=100
while True:
    t=a2//10
    o=a2%10
    n=t+o
    cycle+=1
    a2=10*o+n%10
    if a2==a1:
        break
print(cycle)
