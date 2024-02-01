u =int(input('Enter a number :'))
for i in range(1,u):
    for j in range(1,u):
        if i == 1 or j == 1  or i == 4 or j == 4 :
            print(end= ' * ')
        else:
            print(end= '   ')
    print()