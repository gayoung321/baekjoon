h, m, s = map(int,input().split())
d = int(input())
f = h*3600+m*60+s+d
s = f%60
k = f//60
m = k%60
h = k//60
h %= 24

print(h, m, s)
