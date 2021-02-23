
init -1 python:

    def getRandomColor():
        import random
        random_number = random.randint(1118481,16777215)
        hex_number = str(hex(random_number))
        hex_number ='#'+ hex_number[2:]
        return hex_number

screen mosaic():

    default googleDoc = None

    grid 20 10:

        for x in range(200):

            add Solid( getRandomColor() ):
                size (96, 108)

    timer 1.5 action Function(renpy.restart_interaction) repeat True

label start:

    call screen mosaic