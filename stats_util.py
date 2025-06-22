import json

def level_up(stats, lvl):
    lvl+=1
    for x in range(3):
        print("Which stat do you want to increase?")
        choice = input()

        if choice in stats:
            stats[choice] += 1
            print("Your stats: ",stats)

        elif choice == "save":
            save_stats(stats)

        elif choice == "load":
            stats = load_stats()

        elif choice == "end":
            exit()

        else:
            print("No possible action on input")
            x-=1
    return lvl

def load_stats(filename="stats.json"):
    with open(filename,'r') as savef:
        stats = json.load(savef)
        print("Stats loaded:",stats)
        return stats

def save_stats(stats, filename="stats.json"):
    with open(filename,'w') as loadf:
        json.dump(stats, loadf)
        print("Stats saved:",stats)