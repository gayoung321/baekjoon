a=int(input())
dicta = {}
lista=[]
for _ in range(a):
    temp=input()
    if temp in dicta:
        dicta[temp]+=1
    else:
        dicta[temp]=1
maxd=max(dicta.values())
for book, count in dicta.items():
    if count==maxd:
        lista.append(book)
lista.sort()
print(lista[0])
