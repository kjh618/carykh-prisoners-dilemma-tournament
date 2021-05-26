import numpy as np

def strategy(history, memory):
    NUM_CHANGES = 4
    CHANGE = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): 2,
        (1, 1): 3,
    }
    turn = len(history[0])

    if turn == 0:
        memory = { 'reactions': np.zeros((NUM_CHANGES, NUM_CHANGES)) }
        return 1, memory
    elif turn <= 2:
        return history[1, -1], memory

    reactions = memory['reactions']
    myChange = CHANGE[history[0][turn - 3], history[0][turn - 2]]
    opponentReaction = CHANGE[history[1][turn - 2], history[1][turn - 1]]
    reactions[myChange][opponentReaction] += 1

    # print('-' * 50)

    totalReactions = np.sum(reactions, axis=1)
    # print(totalReactions)

    if not np.all(totalReactions >= 5): # not enough information -> TFT
        return history[1, -1], memory

    reactionRatios = np.full((NUM_CHANGES, NUM_CHANGES), np.nan)
    for i in range(NUM_CHANGES):
        for j in range(NUM_CHANGES):
            reactionRatios[i][j] = reactions[i][j] / totalReactions[i]
    # print(reactionRatios)

    reactionStds = np.std(reactionRatios, axis=0)
    # print(reactionStds)

    if np.all(reactionStds < 0.2): # opponent looks like random -> defect
        return 0, memory
    else:
        return history[1, -1], memory
