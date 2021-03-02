
init -1 python:

    def getRandomColor():
        import random
        random_number = random.randint(1118481,16777215)
        hex_number = str(hex(random_number))
        hex_number ='#'+ hex_number[2:]

        return hex_number

    realCounter = 0.0
    intCounter = 0

    def timeControlFunction(trans, st, at):
        store.realCounter = at
        return None

transform timeControl:
    function timeControlFunction
    pause 0.1
    repeat

screen mosaic():

    timer 1.0:
        action [ SetScreenVariable("changeHexCodes", True), SetVariable("store.intCounter", int(store.intCounter + 1) ) ]
        repeat True

    default changeHexCodes = True
    if changeHexCodes:
        $ changeHexCodes = False
        $ hexcodes = []
        for color in range(200):
            $ hexcodes.append( getRandomColor() )

    grid 20 10:

        for x in range(200):

            add Solid( hexcodes[x] ):
                size (96, 108)

    frame:
        xsize 700
        padding (10, 10)
        xalign 0.5
        at timeControl
        vbox:
            xalign 0.5
            spacing 5
            text ( "Time that should be: " + str( store.intCounter ) ) xalign 0.5
            text ( "Real time: " + str(store.realCounter) ) xalign 0.5
            text ( "Offset: " + str( store.intCounter - store.realCounter ) ) xalign 0.5

label start:

    call screen mosaic