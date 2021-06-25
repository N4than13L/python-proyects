import random


minNumber = 1
maxNumber = 30

print('¿Cual es tu nombre?')
username = str(input())

number = random.randint(minNumber, maxNumber)
print('Bueno ' + username + ' ' + 'Estoy pensando en un numero entre ' + str(minNumber) + ' y ' + str(maxNumber))
dificultad = str(input("inroduce una dificultad: \n"))


def Facil():
    gueesTaken = 0
    while gueesTaken < 2:
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

def medio():
    gueesTaken = 0
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

def Dificil():
    gueesTaken = 0 
    while gueesTaken < 2:
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

if dificultad == "dificil":
    Dificil()
elif dificultad == "medio":
    medio()
elif dificultad == "facil":
    Facil()
else:
    print("dificultad no definida.")