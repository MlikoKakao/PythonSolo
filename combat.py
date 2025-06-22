import player
from enemy import Enemy

enemy = Enemy(player.lvl)

def punch():
    if player.stats["str"] > 1:
        dmg = player.stats["str"] * 20
        print("You hit for ", dmg," HP!")
    else:
        dmg = 1
        print("You're too weak! You barely tickled it for ",dmg," HP!")
    enemy.ehp -= dmg

def fireball():
    if player.stats["ap"] > 1:
        dmg = player.stats["ap"] * 15
        print("You hit for ", dmg," HP!")
    else:
        dmg = 1
        print("You're too weak! You barely tickled it for ",dmg," HP!")
    enemy.ehp -= dmg
    enemy.on_fire = True
    enemy.firedmg = dmg*0.4

    print("The enemy is on fire taking ", enemy.firedmg, " DMG each round!")




def enemy_combat():
    print("You found an enemy!")
    xpup = enemy.ehp * 0.2
    while enemy.ehp > 0:
        if enemy.on_fire:
            enemy.burning(enemy.firedmg)
        print("Enemy has ", enemy.ehp, " HP!")
        print("Which attack do you use?")
        print("Punch, Fireball")
        move = input()

        if move == "punch":
            punch()
        elif move == "fireball":
            fireball()
    player.xp +=xpup
    print("The enemy died!")
    print("You won and got ", xpup," XP!")
    if player.xp > 100:
        player.lvl +=1
        print("You are now level ",player.lvl, "!")
        player.level_up(player.stats,player.stats)