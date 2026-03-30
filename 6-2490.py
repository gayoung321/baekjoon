for _ in range(3):
    y = sum(map(int, input().split()))
    
    if y == 3:
        print('A')
    elif y == 2:
        print('B')
    elif y == 1:
        print('C')
    elif y == 0:
        print ('D')
    else:
        print('E')
    
