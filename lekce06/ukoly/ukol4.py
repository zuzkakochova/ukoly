#Čím se liší chyby, které dostaneš když zadáš tyhle příkazy?

Chyby se liší v nesprávném zápisu proměnných.

int('blabla')
ValueError: invalid literal for int()
správné řešení:
int(input('blabla'))

float('blabla')
ValueError: could not convert string
správné řešení:
float(input('blabla'))

int('8.9')
ValueError: invalid literal for int()
správné řešení:
int(input('8.9'))

int(8.9)
- nic se nevypíše
