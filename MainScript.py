import random

#Public variables

#Draw Lists
singledraw = []
drawsession = []

#Mostdrawn number lists
saturday = [49, 32, 6, 26, 38, 3, 31, 27, 42, 33, 48, 17, 41, 11, 47, 37, 2, 36, 9, 5]
wednesday = [6, 22,13, 33, 31, 38, 26, 16, 11, 32, 10, 25, 34, 4, 7, 41, 19, 14, 28, 36]
satwedcombined = [6, 32, 49, 26, 38, 31, 33, 22, 3, 11, 43, 42, 25, 41, 36, 9, 27, 7, 17, 48]

#Parameter
repetitions = 3
loops = 4

def checktop20(selector):
    check = []

    if selector == "sa":
        check = saturday
    elif selector == "we":
        check = wednesday
    elif selector =="all":
        check = satwedcombined

    while len(singledraw) <= loops:
        # Generate random number
        drawnnumber = random.randint(1, 49)

        # Check drawn number is in list
        if drawnnumber in check:
            # Check drawn number is in list
            if not drawnnumber in singledraw:
                singledraw.append(drawnnumber)


def drawnumbernormallotto():

    checktop20("sa")

    for x in range(repetitions):
        while len(singledraw) < 6:

            #Generate random number
            drawnnumber = random.randint(1, 49)

            #Check drawn number is in list
            if not drawnnumber in singledraw:
                singledraw.append(drawnnumber)
        singledraw.sort()
        drawsession.append(str(singledraw))
        singledraw.clear()
    print(drawsession)
    drawsession.clear()


drawnumbernormallotto()