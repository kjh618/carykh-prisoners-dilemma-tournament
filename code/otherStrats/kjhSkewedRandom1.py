import random

def strategy(history, memory):
    if random.random() < 0.8:
        return 1, None
    else:
        return 0, None
