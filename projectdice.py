import random
from playsound import playsound as music
import time
import pdb


def action(choice):
    player_total = bot_total = 0  # Total outcome of player and the computer
    print("Okay! Go for it!")
    time.sleep(1)
    for no_of_dice in range(0, choice):
        music('shakedice.wav')
        music('rolldice.wav')
        player = random.randint(1, 6)
        time.sleep(1)
        print("You got: ", player)
        player_total += player
        time.sleep(1)
    print("\n YOUR TOTAL IS: ", player_total)
    time.sleep(1)
    print("\nNow it's opponent's turn")
    time.sleep(1)

    for no_of_dice in range(0, choice):
        music('shakedice.wav')
        music('rolldice.wav')
        bot = random.randint(1, 6)
        time.sleep(1)
        print("He got: ", bot)
        bot_total += bot
        time.sleep(1)
    print("\n HIS TOTAL IS: ", bot_total)
    time.sleep(2)

    result = "\nYou Win. YAYYYYYYY!" if player_total > bot_total else "\nHE WON! YOU LOSEEE :( " if bot_total > player_total \
        else "\nTIE. PLAY AGAIN"
    print(result)
    if player_total > bot_total:
        music('win.wav')
    elif bot_total > player_total:
        music('lose.mp3')
    time.sleep(1)


def play():
    no_of_dice = 0  # dice takes integer
    roll = ' '  # roll takes string
    while no_of_dice == 0:
        print('WELCOME TO DICE GAME. HAPPY PLAYING')
        time.sleep(1)
        choice = int(input("How many dice you want to throw (1-3)? "))
        if choice > 0 and choice < 4:
            action(choice)
            break
        else:
            print("Please enter the valid choice between 1 to 3!!!!!")
    print("\n Do you want to continue?(yes/no)")
    while roll != "Yes":
        roll = input().lower().capitalize()
        if roll == "Yes":
            play()
        else:
            print("It was nice playing with you. See you again.")
            time.sleep(1)
            break


play()
