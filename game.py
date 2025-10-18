import random

rdm = random.randint(1, 1000)
inputUser = -1
arr = []

while inputUser != rdm:

    inputUser = int(input("Введитечисло от 1 о 1000:"))

    arr.append(inputUser)
    print(f"Вы вводили :{arr}")

    if inputUser <= 1000 and inputUser >= 0:
        if inputUser == rdm:
            print("успех")
            continue
        elif inputUser <= rdm:
            print("меньше")
        elif inputUser >= rdm:
            print("больше")
    else:
        print("чето ты плохо ввел")