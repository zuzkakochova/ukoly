#Pomocí cyklů for a příkazu if napiš program, který z jednotlivých 'X' a mezer vypíše:

for i in range(6):
    if i == 0 or i == 5:
        for j in range(6):
            print('X' , end=' ')
    else:
        for j in range(6):
            if j == 0 or j == 5:
                print('X' , end=' ')
            else:
                print(' ' , end=' ')
    print()
