nombre = int(input('Donnez un nombre : '))
for i in range(1,nombre+1):
    if nombre%i==0:
        print(i)