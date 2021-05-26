import numpy as np

def strategy(history, memory):
    turn = len(history[0])
    # BAR = '-' * 20
    # print(f'{BAR} Turn {turn} {BAR}')

    if turn == 0:
        memory = { 'reactions': np.zeros((2, 2)) }
        return 1, memory
    elif turn == 1:
        return history[1][-1], memory

    # Record the opponent's reaction to my move in the previous turn.
    reactions = memory['reactions']
    myMove = history[0][-2]
    opponentReaction = history[1][-1]
    reactions[myMove][opponentReaction] += 1
    # print(f'reactions: \n{reactions}')

    # Not enough information -> TFT
    if np.any(reactions < 3):
        return history[1][-1], memory

    # Calculate the propotions of the opponent's reactions to my moves.
    reactionProportions = np.full_like(reactions, np.nan)
    for my in [0, 1]:
        totalReactions = np.sum(reactions[my])
        for opp in [0, 1]:
            reactionProportions[my][opp] = reactions[my][opp] / totalReactions
    # print(f'reactionProportions: \n{reactionProportions}')
    
    # Calculate the standard deviations of the reaction proportions.
    # FYI, the 2 stds are the same and equal to diff / 2 here.
    reactionDeviations = np.std(reactionProportions, axis=0)
    # print(f'reactionDeviations: \n{reactionDeviations}')

    # Opponent looks like random -> defect
    if np.all(reactionDeviations < 0.1):
        return 0, memory
    else: # Otherwise, TFT
        return history[1][-1], memory
