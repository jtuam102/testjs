#fighting_against_ai
from random import randint
import time


class Gamer:
     

     def getName(player):
         player.name = input("What is your Gamer Tag? ")    

     def callName(player):
         return player.name

     def buildStats(player):
         player.health = 100

     def playerStats(player):
         player.playerStats = [player.name, player.health]
         return player.playerStats


    
     def buildEnemy(player):
         available_names = ["The STRONK BOT", "PRO AI", "WALLER", "LMAO BOT", "CONOR MC BOT", "Randy OrBOT", "TrIggerBOT", "OPen AI", "HaRDcORE AI", "ExPERatSU BOT", "n00b BOT","bruh"]
         player.enemy_name = available_names[randint(0,11)]
         player.enemy_health = 100

     def getEnemy(player):
         player.enemy_stats = [player.enemy_name, player.enemy_health]
         return player.enemy_stats



     def createfight(player):
         player1.getName()
         print("\n")
         player1.buildStats()
         print(player1.playerStats())
         print("VS AGAINST")
         player1.buildEnemy()
         print(player1.getEnemy())
         print("\n")
         print("GOOD LUCK, HAVE FUN!!\n")
         print("The Countdown STARTS!")
         for n in range (5):
             print(5-n)
             time.sleep(1)
         print("FIGHTT!!!\n")



def fight_them():
    type = int(input("What is your move?? (Press 1 for PUNCH, Press 2 for KICK, Press 3 for SPELL, Press 4 for RISKY ULTIMATE, Press 5 for FLEE): "))
    print("\n")
    if type == 1 :
        print(player1.playerStats[0] + " PUNCH " + player1.enemy_stats[0] + " in the FACE!!" )
        attack_damage = int(randint(1,11))
        chance_num = int(randint(0,100))
        if chance_num >= 10:
            player1.enemy_health -= attack_damage
            if player1.enemy_health <= 0 :
                print(player1.enemy_stats[0] + " DIES?!?!")
                print(player1.playerStats[0] + " WINS!! WHAT A VICTORY!!")
            else:
                print(player1.playerStats[0] + " attacks " + player1.enemy_stats[0] + " for " + str(attack_damage) + " damage! ")
                print(player1.enemy_stats[0] + " has " + str(player1.enemy_health) + " health left!! \n")
        else:
            print("NICE, you PUNCHED the air...WHAT A PLAYER LOL!!!!\n")

    if type == 2 :
        print(player1.playerStats[0] + " KICKS " + player1.enemy_stats[0] + " in the freaking GUT!!" )
        attack_damage = int(randint(5,14))
        chance_num = int(randint(0,100))
        if chance_num >= 25:
            player1.enemy_health -= attack_damage
            if player1.enemy_health <= 0 :
                print(player1.enemy_stats[0] + " DIES?!?!")
                print(player1.playerStats[0] + " WINS!! WHAT A VICTORY!!")
            else:
                print(player1.playerStats[0] + " attacks " + player1.enemy_stats[0] + " for " + str(attack_damage) + " damage!! ")
                print(player1.enemy_stats[0] + " has " + str(player1.enemy_health) + " health left to sustain this FIGHT!! \n")
        else:
            print("You SUCK at KICKING!!! ATTACK MISSED! YOU NOOB!!!!\n")

    if type == 3 :
        print(player1.playerStats[0] + " PUTS A SPELL ON " + player1.enemy_stats[0] + "!!" )
        attack_damage = int(randint(7,12))
        chance_num = int(randint(0,100))
        if chance_num >= 20:
            player1.enemy_health -= attack_damage
            if player1.enemy_health <= 0 :
                print(player1.enemy_stats[0] + " DIES?!?!")
                print(player1.playerStats[0] + " WINS!! WHAT A VICTORY!!")
            else:
                print(player1.playerStats[0] + " BURNED " + player1.enemy_stats[0] + " for " + str(attack_damage) + " damage! ")
                print(player1.enemy_stats[0] + " has " + str(player1.enemy_health) + " health left!! \n")
        else:
            player1.health -= attack_damage
            print(player1.playerStats[0] + " CURSED himself " + " for " + str(attack_damage) + " damage! ")
            print("Nice spell, idiot.")
            print(player1.enemy_stats[0] + " has " + str(player1.enemy_health) + " health left!! \n")
            
    if type == 4 :
        print(player1.playerStats[0] + " USES THE RISKY ULTIMATE ON " + player1.enemy_stats[0] + "!!" )
        attack_damage = int(randint(15,20))
        chance_num = int(randint(0,100))
        if chance_num >= 50:
            player1.enemy_health -= attack_damage
            if player1.enemy_health <= 0 :
                print(player1.enemy_stats[0] + " DIES?!?!")
                print(player1.playerStats[0] + " WINS!! WHAT A VICTORY!!")
            else:
                print(player1.playerStats[0] + " STRIKED LIGHTNING ON " + player1.enemy_stats[0] + " for " + str(attack_damage) + " damage! ")
                print(player1.enemy_stats[0] + " has " + str(player1.enemy_health) + " health left!! \n")
        else:
            player1.health -= 15
            print(player1.playerStats[0] + " AIMED AT THE GROUND AND HURT himself " + " for " + "15" + " damage! ")
            print(player1.enemy_stats[0] + " has " + str(player1.enemy_health) + " health left!! \n")


    if type == 5 :
        print(player1.playerStats[0] +  " FLED FROM THE ARENA!! YOU FREAKING COWARD?!!" )
        attack_damage = 100
        player1.health -= attack_damage
        print(player1.enemy_stats[0] + " WINS WITHOUT BREAKING ANY SWEAT HAHA!!!!")
        
    if type != 1 and type != 2 and type != 3 and type != 4 and type != 5:
         print("You DID NOTHING LUL, BRAINS!! \n" )
         
         
    player1.myturn = False
    time.sleep(2)
    return player1.enemy_health

def being_fought():
    print(player1.enemy_stats[0] + " attacks " + player1.playerStats[0] + "!!")
    attack_damage = int(randint(6,14))
    chance_num = int(randint(0,100))
    if chance_num >= 10:
        player1.health -= attack_damage
        if player1.health <= 0 :
            print(player1.playerStats[0] + " GOT CRUSHED BY A BOT!!")
            print(player1.enemy_stats[0] + " IS THE CHAMPION!!!!")
            
        else:
            print(player1.enemy_stats[0] + " locked ON " + player1.playerStats[0] + "!!")
            print(player1.enemy_stats[0] + " STRIKES " + player1.playerStats[0] + " for " + str(attack_damage) + " damage!! ")
            print(player1.playerStats[0] + " is left with " + str(player1.health) + " health!! \n")
    else:
        print("WRONG CALCULATION!! ATTACK MISSED!?! NANI!?!?\n")
    
    player1.myturn = True
    time.sleep(2)
    return player1.health

def during_fight():
    while player1.health > 0 and player1.enemy_health > 0 :
        if player1.myturn == True:
            fight_them()
        elif player1.myturn ==False:
            being_fought()



print("READ THE INSTRUCTIONS!")
print("PUNCH is a move that only deals 1 to 11 damage, but has only 10% chance of missing the attack.")
print("KICK is a crit move that deals 5 to 14 damage, but has 30% chance missing the attack.")
print("SPELL is an advanced move that has a chance of dealing 7 to 12 damage with 20% chance of missing, but YOU might hurt yourself if YOU MISSED!")
print("RISKY ULTIMATE is a high risk high reward move with a 50% chance of missing the attack, it's either you deal a massive 15 to 20 damage or you will damage yourself for 15 damage!")
print("FLEE is to ESCAPE to prove that you are truly a loser.")
print("PS: DO NOT KEY IN ALPHABET LETTERS!")
print("Thanks for being patient and ENJOY!\n")
print("Welcome to FIGHTING AGAINST BOTS ARENA!!")

player1 = Gamer()
player1.createfight()
fight_them()
during_fight()
        
    
    
