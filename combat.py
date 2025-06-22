from logging import critical

import player
import stats_util
from enemy import Enemy
import random

enemy = Enemy(player.lvl)

def punch():
        base_dmg = player.stats["str"] * 20 if player.stats["str"] >= 1 else 1
        crit_chance = player.stats["sns"] * 5
        is_crit = random.randint(1,100) <= crit_chance

        if is_crit:
            dmg = int(base_dmg * 1.5)
            print("CRITICAL HIT! You hit for ",dmg,"HP!")
        else:
            dmg = base_dmg
            if dmg == 1:
                print("You're too weak! You barely tickled it for ",dmg," HP!")
            else:
                print("You hit for", dmg, "HP!")
        enemy.ehp -= dmg

def fireball():
    base_dmg = player.stats["ap"] * 15 if player.stats["ap"] >= 1 else 0
    crit_chance = player.stats["sns"] * 5
    is_crit = random.randint(1,100) <= crit_chance

    if is_crit:
        dmg = int(base_dmg * 1.5)
        print("CRITICAL HIT! You hit for ",dmg,"HP!")
    else:
        dmg = base_dmg
        if dmg == 0:
            print("Why did you think you can cast magic?")
        else:
            print("You hit for", dmg, "HP!")
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

            if enemy.ehp <= 0:
                break

        print("Enemy has ", int(enemy.ehp), " HP!")
        print("Which attack do you use?")
        print("Punch, Fireball")
        move = input()

        if move == "punch":
            punch()
        elif move == "fireball":
            fireball()
    player.xp +=xpup
    print("The enemy died!")
    print("You won and got ", int(xpup)," XP!")
    if player.xp > 100:
        player.lvl = stats_util.level_up(player.stats, player.lvl)
        print("You are now level ",player.lvl, "!")
        stats_util.level_up(player.stats,player.lvl)
    enemy.ehp += 100 + (1.2*player.xp)
    enemy.on_fire = False