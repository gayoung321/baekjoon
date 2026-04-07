dicta={}
lista=[]
n=int(input())
for i in range(n):
    tempkey, tempvalue=input().split()
    dicta[tempkey]=tempvalue
for j in dicta:
    if dicta[j]=='enter':
        lista.append(j)
lista.sort(reverse=True)
for k in lista:
    print(k)
