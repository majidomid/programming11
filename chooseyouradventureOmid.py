import random
import time
def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')#intro message for the game
    print()

def chooseCave():
    cave = ''
    while cave!= '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input() #intial choice 50% chance of winning

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!') #win the 50/50 roll
        escape = ''
        while escape != '1' and escape != '2':
            print("A group of raiders are aware of your treasure and have started chasing you!")
            time.sleep(1)
            print("Which path will you take to escape? (1 or 2)")
            escape = input() #2nd choice 50% chance of winning (25% chance overall of winning at this point)
            print("You begin to dash away...")
            time.sleep(2)
            print("The raiders are gaining on you...")
            time.sleep(2)
            print("Youre approaching an uphill climb and...")
            print()
            time.sleep(2)

            goodEscape = random.randint(1, 2)

            if str(goodEscape) == str(escape) :
                print("You clear the hill and leave the raiders in the dust.") #win 50/50 roll
                time.sleep(1)
                print("Do you perform a victory taunt to anger the raiders? (yes or no)")
                taunt = input() #simple yes/no. yes always loses
                if taunt == "yes" or taunt == "y":
                    print("You moon the raiders and one of them quickly shoots an arrow where the sun doesn't shine. You die.")
                else:
                    print("You stick to your senses and waste no time getting as far away from the raiders as possible.")
                    decision = ''
                    while decision == '':
                        
                        time.sleep(2)
                        print("On your way back to your ship, you stumble upon an conniving old wizard")
                        time.sleep(1)
                        print("The wizard introduces himself and asks you a riddle that none could solve before him")
                        print('"What is something a man cannot live his life without; the juice?, or the sauce?"(j or s)')
                        decision = input()#simple yes/no "j" always loses.
                        if decision == 'j':
                            print('The wizard shoots you in the chest and proclaims "The juice is only temporary while the sauce is eternal". You died.')
                        if decision == 's':
                            print('The wizard shoots himself in the chest and proclaims "I have been bested, take my staff of power wise one". You take his staff and go on your way.')
                        if decision != 'j' and decision != 's':
                            print("Stick to the rules you fool! The wizard shoots you in the chest.")#lose if they dont answer within the perimeters stated
                        
                    
            else:
                print("You trip and fall, the raiders catch you and leave nothing behind. (Not even your dignity)") #lose 2nd 50/50 roll
    else:
        print('Gobbles you down in one bite') #lose initial 50/50 roll

        

playAgain = 'yes' #reset if they choose to play again
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)


    print('Do you want to play again? (yes or no)')
    playAgain = input()
    
