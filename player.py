import stats_util


xp = 0

stats = {
    "hp": 0,
    "str": 0,
}

def level_up():
    for x in range(3):
        print("Which stat do you want up?")
        choice = input()

        if choice in stats:
            stats[choice] += 1
            print("Wow look at your stats!",stats)

        elif choice == "save":
            stats_util.save_stats(stats)

        elif choice == "load":
            stats = stats_util.load_stats()

        elif choice == "end":
            exit()

        else:
            print("No possible action on input")