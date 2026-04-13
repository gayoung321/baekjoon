import sys
input=sys.stdin.readline
a, b = map(int, input().split())
dicta={}
lista=[]
for i in range(b):
    temp=input().strip()
    dicta[temp]=i
for id,num in dicta.items():
    lista.append([num,id])
lista.sort()
for j in range(min(a, len(lista))):
    print(lista[j][1])
