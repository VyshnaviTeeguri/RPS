# RPS.py

import random

# Function to store opponent history and make predictions
def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # Initial move
    if not opponent_history:
        return "R"

    # Strategies for different opponents
    counter_move = {"R": "P", "P": "S", "S": "R"}

    # Simple pattern recognition strategy
    if len(opponent_history) >= 3:
        last_three = "".join(opponent_history[-3:])
        if last_three == "RRR":
            return "P"
        elif last_three == "PPP":
            return "S"
        elif last_three == "SSS":
            return "R"

    # Random move as a fallback
    return counter_move[opponent_history[-1]]
