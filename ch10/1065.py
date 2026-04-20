a = int (input())
count = 0
if a<100:
    print(a)
else:
    for i in range(100, a+1):
        lista = []
        while i>0:
            b = i%10
            i = i//10
            lista.append(b)
        if lista[1]-lista[0] == lista[2]-lista[1]:
            if lista[2] != 0:
                count +=1
    print (99+count)
