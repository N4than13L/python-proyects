import random

gueesTaken = 0 
minNumber = 1
maxNumber = 30

print('¿Cual es tu nombre?')
username = str(input())

number = random.randint(minNumber, maxNumber)
print('Bueno ' + username + ' ' + 'Estoy pensando en un numero entre ' + str(minNumber) + ' y ' + str(maxNumber))

while gueesTaken < 5:
    print('adivina un numero entre' + ' ' + str(minNumber) + ' y ' + str(maxNumber))
    guees = int(input())
    gueesTaken = gueesTaken + 1

    if guees < number:
        print('Tu numero es demasiado bajo.')

    elif guees > number:
        print('Tu numero es demasiado alto.')

    elif guees == number:
        print('¡buen trabajo ' + username + 'tu has adivinado en' + ' ' + str(gueesTaken) + ' ' + 'intentos!')
        print('No es el valor que estaba pensando en el numero' + ' ' + str(number)) 
        break 