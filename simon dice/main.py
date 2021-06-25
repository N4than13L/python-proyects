import random
import os
import time

colors = "RGBY"
simon = ""

for score in range(0,10):
    simon += random.choice(colors)
    for color in simon:
        print(color)
        time.sleep(1.5)
        os.system("cls")
    guees = input("repite: ")
    os.system("cls")

    if guees != simon:
        break
    print(f"Perdiste tu puntaje es: {score}!")