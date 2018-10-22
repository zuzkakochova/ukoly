#Napiš program, který postupně z jednotlivých 'X' vypíše:

for i in range(5):
    for j in range(i):
        print( 'X' , end=' ')
    print()
