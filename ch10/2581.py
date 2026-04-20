a = int (input())
b = int(input())
summ = 0
lista=[]
for num in range(a, b+1):
    if num>1:
        k = int(num**0.5)
        y = True
        for i in range(2,k+1 ):
            if num%i ==0:
                y = False
                break
        if y == True:
            lista.append(num)
if lista == []:
    print(-1)
else:
    summ = sum(lista)
    mini = lista[0]
    print (summ)
    print(mini)
