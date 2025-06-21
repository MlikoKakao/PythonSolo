import json


def load_stats(filename="stats.json"):
    with open(filename,'r') as f:
        stats = json.load(f)
        print("Stats loaded:",stats)
        return stats

def save_stats(stats, filename="stats.json"):
    with open(filename,'w') as f:
        json.dump(stats, f)
        print("Stats saved:",stats)