                  ###########TRESURER########
                  #This game is about a tresurer who is trying o find a tresure#
                  #But in the cave he found some opsticles which might make it harder for him to find the gold. See if you could help him with finding it!!###
                  #energy- you should keep track of it. If you run out of it you would die in the cave#
def start():
    print("Welcome, you are a tresurer. And you are trying to find a gold tresure from a mysterious cave. The most important thing that you should keep track of is your energy(10 energy points).")
    print()
    cave_entr()

def cave_entr():
    print()
    if tresure is True:
            print("Congratulations, you won the tresure")
            exit()
    move = input("\nWhen you enter the cave you have two decision? Wheter go:\n\tleft\n\tright\n")
    if move.lower() == "left":
        left()
    elif move.lower() == "right":
        right()
    

    else:
        
        print("\nI don't understand your input, I will assume that you want to stay here")
        
def left():
    global energy
    energy = energy - 3
    if energy <= 0:
        print("sorry, you ran out of energy. You lost the game")
        exit()

    print("Energy is now ",energy)
    print("You went on a long and exhousting investigation of the left part of the cave. Unfortunatly the only thing that you found is a useless abyss")
    move = input("\nAfter this long investigation you lost a lot of energy points and the only option that you have is to go back to the cave entarnce? type:\ncave_entr\n")
    if move.lower() == "cave_entr":
        cave_entr()
    elif move.lower() == "room3":
        room3()
    else:
        print("I'm not sure that I understood your input, I will assume that you want to stay here")

def right():
    global energy
    energy = energy -2
    if energy <= 0:
        print("sorry, you ran out of energy. You lost the game")
        extit()
    print("your energy is now",energy)
    print("You decided to go to the right part of the cave. And you found an abandoned mine. From there you have two curves. The right one looks longer and more stable than the left one. But the left curve is smaller and looks extremely dangerous. ")
    move = input("\nWould you take the risk or stay safe? choices:\n\tcurve_left\n\tcurve_right\n")
    if move.lower() == "curve_left":
        curve_left()
    elif move.lower() == "curve_right":
        curve_right()
    else:
        #TODO: what should happen if they type something else?
        print("I don't understand your input, I will assume that you want to stay here")
def curve_left():
    global energy 
    energy = energy-2
    if energy <= 0:
        print("sorry, you ran out of energy. You lost the game")
        exit()
    global tresure
    tresure= True
    print("After you took the risk and went to the left curve, you ended up with finding the tresure now you need to bring it back to the entrance cave without running out of energy, your energy is", energy)
    if energy <= 0:
        print("sorry, you ran out of energy. You lost the game")
        exit()
    move = input("\nGo back to:\ncave_entr\n")
    if move.lower()=="cave_entr":
        cave_entr()


def curve_right():
    global energy
    energy = energy-4
    if energy <= 0:
        print("sorry, you ran out of energy. You lost the game")
        exit()
    print("After you chose the safest option, you went to the longer cave but you got lost during that investigation, after you found the right way you ended up with loosing a lot of points, your energy is",energy)
    move = input("\nGo to:\ncurve_left\ncurve_right\n")
    if move.lower()=="curve_left":
        curve_left()
    elif move.lower()=="curve_right":
        curve_right()
########
#main
#######
#TODO: Add some global variables
energy = 10
tresure = False
start()
