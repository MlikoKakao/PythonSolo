import json


def load_stats(filename="stats.json"):
    with open(filename,'r') as savef:
        stats = json.load(savef)
        print("Stats loaded:",stats)
        return stats

def save_stats(stats, filename="stats.json"):
    with open(filename,'w') as loadf:
        json.dump(stats, loadf)
        print("Stats saved:",stats)