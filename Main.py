import json
import stats_util
import player
import combat

print("Initial stats:",player.stats)
for x in range(5):
    stats_util.level_up(player.stats, player.lvl)

    combat.enemy_combat()





