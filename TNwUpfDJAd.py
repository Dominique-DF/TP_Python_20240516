nombre = int(input('Donnez un nombre : '))
nb = nombre # on recopie le nombre pour pouvoir en garder une copie tout en le divisant
i = 2 # on commence par le premier diviseur possible soit 2
repet = 0 # on compte combien de fois on divise par diviseur
while nb>1: # tant qu'on peut continuer à le diviser
    if nb%i==0:
        repet = repet+1
        nb = nb/i
    elif repet != 0:
        print(f'{i}^{repet}')
        i = i+1
        repet = 0
    else:
        i = i+1
if i != nombre:
    print(f'{i}^{repet}')
else:
    print(f'{nombre} est premier')