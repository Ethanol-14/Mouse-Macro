from pynput.keyboard import Key, Controller as KeyCon
from pynput.mouse import Button, Controller as ButCon
import keyboard
import time

keys = KeyCon()
mouse = ButCon()

inputs = []
delay = 0.017

print("Press 1 to add a hold click to the list")
print("Press 2 to add an unclick to the list")
print("Press q to add the current mouse position to the list")
print("Press w to add position, unclick, click, to the list")
print("Press e to print the list")
print("Press a to clear the inputs list")
print("Press r to run the inputs")
print("Press s to export the current inputs list to inputs.txt")
print("Press d to import the inputs from inputs.txt to the current inputs list")
print("Press f to replay this message")

while True:
    #turns out computer starts having high cpu because it'll just run the code as fast as possible lol
    #simply a delay
    time.sleep(0.02)

    if keyboard.is_pressed("1"):
        #add a hold click to the list
        inputs.append("lcl")
        print("added clicked")

        while keyboard.is_pressed("1"):
            time.sleep(0.02)

    if keyboard.is_pressed("2"):
        #add an unclick to the list
        inputs.append("luncl")
        print("added unclicked")

        while keyboard.is_pressed("2"):
            time.sleep(0.02)

    if keyboard.is_pressed("q"):
        #add the mouse's current position to the list
        inputs.append(mouse.position)
        print("added current mouse position")

        while keyboard.is_pressed("q"):
            time.sleep(0.02)

    if keyboard.is_pressed("w"):
        #add position, unclick, click
        inputs.append(mouse.position)
        inputs.append("luncl")
        inputs.append("lcl")
        print("added position, unclicked, clicked")

        while keyboard.is_pressed("w"):
            time.sleep(0.02)

    if keyboard.is_pressed("e"):
        #review inputs list
        print(inputs)
        
        while keyboard.is_pressed("e"):
            time.sleep(0.02)

    if keyboard.is_pressed("a"):
        #clear the list of inputs and ask for confirmation of action
        print("clear saved inputs? y/n")

        while not (keyboard.is_pressed("y") or keyboard.is_pressed("n")):
            time.sleep(0.02)

        if keyboard.is_pressed("y"):
            inputs.clear()
            print("inputs cleared")

        else:
            print("inputs not cleared")

    if keyboard.is_pressed("r"):
        while keyboard.is_pressed("r"):
            time.sleep(0.02)
    
        #the the inputs
        print("running")

        #check what's written then execute per line
        for n in inputs:
            if n == "lcl":
                mouse.press(Button.left)
                print("click")

            elif n == "luncl":
                mouse.release(Button.left)
                print("unclick")

            else:
                mouse.position = n
                print("move")
            time.sleep(delay)
            
            if keyboard.is_pressed("esc"):
                break

        print("finished")

    if keyboard.is_pressed("s"):
        #just to check in case s was a finger slip
        print("do you want to export your inputs? y/n")

        while not (keyboard.is_pressed("y") or keyboard.is_pressed("n")):
            time.sleep(0.02)

        if keyboard.is_pressed("y"):
            print("exporting inputs")

            #to clear the file
            #probably not the most efficient way but I don't know other ways :P
            file = open("inputs.txt", "w")
            file.close()

            file = open("inputs.txt", "a")

            count = 0
            #for some reason for loops don't work here so I just did this :P
            while count < len(inputs):
                temp = inputs[count]
                #the "\n" tells python to write each string on a new line in the "notepad"
                file.write(str(temp) + "\n")
                count = count+1

            file.close()
            print("inputs exported succesfully")

        else:
            print("inputs not exported")

    if keyboard.is_pressed("d"):
        #same check as before
        print("do you want to import inputs from inputs.txt? y/n")

        while not (keyboard.is_pressed("y") or keyboard.is_pressed("n")):
            time.sleep(0.02)

        if keyboard.is_pressed("y"):
            print("importing inputs")

            #"r" because we're only importing, no need to write, just read
            file = open("inputs.txt", "r")
            inputs.clear()

            #this is to load the file into my list called "inputs"
            for n in file:
                inputs.append(n)

            print("processing inputs")

            #remove the "\n", the "(", and the ")", because for some weird reason python puts "\n" to means "new line"
            #the brackets are removed so that I can make the mouse coordinates into tuples later
            count = 0
            while count < len(inputs):
                temp = inputs[count]
                temp = temp.replace("\n", "")
                inputs[count] = temp
                count = count+1

            count = 0
            while count < len(inputs):
                temp = inputs[count]
                temp = temp.replace("(", "")
                inputs[count] = temp
                count = count+1

            count = 0
            while count < len(inputs):
                temp = inputs[count]
                temp = temp.replace(")", "")
                inputs[count] = temp
                count = count+1

            #now we turn everything that isn't "cl" or "uncl" into a tuple
            #I know there's a ", " between the two numbers so I split it from that
            count = 0
            while count < len(inputs):
                temp = inputs[count]
                if temp != "lcl" and temp != "luncl":
                    temp = tuple(map(int, temp.split(", ")))
                    inputs[count] = temp
                
                count = count+1

            print("inputs successfully imported")

        else:
            print("inputs not imported")
            
    if keyboard.is_pressed("f"):
        print("Press 1 to add a hold click to the list")
        print("Press 2 to add an unclick to the list")
        print("Press q to add the current mouse position to the list")
        print("Press w to add position, unclick, click, to the list")
        print("Press e to print the list")
        print("Press a to clear the inputs list")
        print("Press r to run the inputs")
        print("Press s to export the current inputs list to inputs.txt")
        print("Press d to import the inputs from inputs.txt to the current inputs list")
        print("Press f to replay this message")
        
        while keyboard.is_pressed("f"):
            time.sleep(0.02)
