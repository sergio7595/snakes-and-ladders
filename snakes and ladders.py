
#-------------------------------------------------------------------------------
# Name:        snakes and ladders
# Purpose:
#
# Author:      sergio drumond gutierrez (7595)
#
# Created:     08/05/2017
# Copyright:   (c) 7595 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random,sys
#this is the whole game line of code
player = 0
computer = 0

def game():


    enter= int(input("hello press 1 for play or 2 to quit"))


    def startmenu():
        if enter == 1:
            print("well onto the board")
        elif enter == 2:
            exit()
        else:
            print("hmmmmmmm try again moron")
            startemenu
    startmenu()

    def userinput():
        def inputlol():
            player = int(input("enter 1 for roll or 2 to forfit"))
            add = random.randint(0,7)
            computer = computer + add
            if player == 1:
                add2 = random.randint(0,7)
                player = player + add2
            elif player == 2:
                exit()
            else:
                userinput()
            print ("your in position",player,"the pc is on position",computer)
        inputlol()
        def boards():
            if player == 4:
                print ("oh a ladder")
                player = player + 10
            elif player == 9:
                print ("oh a ladder")
                player = player + 22
            elif player == 17:
                print ("dam snake")
                player = player - 10
            elif player == 20:
                print ("oh a ladder")
                player = player + 18
            elif player == 28:
                print ("oh a ladder")
                player = player + 56
            elif player == 40:
                print ("oh a ladder")
                player = player + 19
            elif player == 51:
                print ("oh a ladder")
                player = player + 16
            elif player == 54:
                print ("dam snake")
                player = player - 20

        while player < 100 and computer < 100:
            inputlol()
        boards()

        if player >= 100:
            print("you win person")
        elif computer >= 100:
            print("well done you faced a beast and lost")
    userinput()

game()


