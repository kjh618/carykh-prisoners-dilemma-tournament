import numpy as np

def strategy(history, memory):
    """Tit-for-tat but detect random and defect."""

    turn = len(history[0])
    if turn == 0:
        memory = {
            'reactions': np.zeros((2, 2)),
            'isOpponentRandom': False,
        }
        return 1, memory
    elif turn == 1:
        return history[1][-1], memory

    # Record the opponent's reaction to my move in the previous turn.
    reactions = memory['reactions']
    myMove = history[0][-2]
    opponentReaction = history[1][-1]
    reactions[myMove][opponentReaction] += 1

    # Not enough information -> TFT
    totalReactions = np.sum(reactions, axis=1)
    if not np.all(totalReactions >= 5):
        memory['isOpponentRandom'] = False
        return history[1][-1], memory

    # Calculate the propotions of the opponent's reactions to my moves.
    reactionProportions = np.full_like(reactions, np.nan)
    for my in [0, 1]:
        for opp in [0, 1]:
            reactionProportions[my][opp] = reactions[my][opp] / totalReactions[my]
    
    # Calculate the standard deviations of the reaction proportions.
    # FYI, the 2 stds are the same and equal to diff / 2 here.
    reactionDeviations = np.std(reactionProportions, axis=0)

    # If the opponent looks like random, defect. Otherwise TFT.
    if np.all(reactionDeviations < 0.1):
        memory['isOpponentRandom'] = True
        return 0, memory
    else:
        if memory['isOpponentRandom']:
            # Reinitiate TFT
            memory['isOpponentRandom'] = False
            return 1, memory
        else:
            # Continue TFT
            memory['isOpponentRandom'] = False
            return history[1][-1], memory
