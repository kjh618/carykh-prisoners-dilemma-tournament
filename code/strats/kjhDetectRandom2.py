import numpy as np

def strategy(history, memory):
    """Tit-for-tat but detect random and defect. Also forgives one-off defects."""

    def isRandom(reactionProportions):
        # Calculate the standard deviations of the reaction proportions.
        # FYI, the 2 stds are the same, and equal to diff / 2 here.
        reactionDeviations = np.std(reactionProportions, axis=0)
        return np.all(reactionDeviations < 0.1)
    
    def isTft(reactionProportions):
        cooperative = reactionProportions[1][1] >= 5 * reactionProportions[1][0]
        retaliating = reactionProportions[0][0] >= 5 * reactionProportions[0][1]
        return cooperative and retaliating

    turn = len(history[0])
    if turn == 0:
        memory = {
            'reactions': np.zeros((2, 2)),
        }
        return 1, memory
    elif turn == 1:
        return history[1][-1], memory

    # Record the opponent's reaction to my move in the previous turn.
    reactions = memory['reactions']
    myMove = history[0][-2]
    opponentReaction = history[1][-1]
    reactions[myMove][opponentReaction] += 1

    # If there's not enough information, TFT.
    totalReactions = np.sum(reactions, axis=1)
    if not np.all(totalReactions >= 5):
        return history[1][-1], memory

    # Calculate the propotions of the opponent's reactions to my moves.
    reactionProportions = np.full_like(reactions, np.nan)
    for my in [0, 1]:
        for opp in [0, 1]:
            reactionProportions[my][opp] = reactions[my][opp] / totalReactions[my]

    # If the opponent looks like random, defect.
    if isRandom(reactionProportions):
        return 0, memory

    # If the opponent looks like TFT but defected last turn,
    # cooperate to prevent CD/DC loop.
    if isTft(reactionProportions) and history[1][-1] == 0:
        return 1, memory
    
    # Otherwise, TFT.
    return history[1][-1], memory
