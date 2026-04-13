import sys
input=sys.stdin.readline
a, b = map(int, input().split())
aset=set()
bset=set()
clist=[]
for _ in range(a):
    hear=input().strip()
    aset.add(hear)
for _ in range(b):
    see=input().strip()
    bset.add(see)
clist=list(aset & bset)
print(len(clist))
clist.sort()
for i in clist:
    print(i)
