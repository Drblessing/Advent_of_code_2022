# Day 2: Part One
# Rock paper scissors
# Read input
with open("input.txt") as f:
    data = f.read().splitlines()

# Define point values for each choice
choices_to_points = {"rock": 1, "paper": 2, "scissors": 3}
letter_to_choices = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}
outcome_to_points = {"win": 6, "lose": 0, "draw": 3}

# Iterate over each game
# adding score to total
total_score = 0
for game in data:
    opponent_choice = letter_to_choices[game[0]]
    my_choice = letter_to_choices[game[2]]

    # Calculate Score
    # Draw
    if opponent_choice == my_choice:
        total_score += outcome_to_points["draw"] + choices_to_points[my_choice]
    # Win
    elif (
        (my_choice == "scissors" and opponent_choice == "paper")
        or (my_choice == "paper" and opponent_choice == "rock")
        or (my_choice == "rock" and opponent_choice == "scissors")
    ):
        total_score += outcome_to_points["win"] + choices_to_points[my_choice]
    # Lose
    else:
        total_score += outcome_to_points["lose"] + choices_to_points[my_choice]
print(total_score)

# Day 2: Part Two
# Rock paper scissors
# Read input
with open("input.txt") as f:
    data = f.read().splitlines()

# Define point values for each choice
choices_to_points = {"rock": 1, "paper": 2, "scissors": 3}
letter_to_choices = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}
outcome_to_points = {"win": 6, "lose": 0, "draw": 3}
letter_to_outcome = {"X": "lose", "Y": "draw", "Z": "win"}


# Iterate over each game
# adding score to total
total_score = 0
for game in data:
    opponent_choice = letter_to_choices[game[0]]
    outcome = letter_to_outcome[game[2]]

    # Calculate my choice based on the outcome and opponent choice
    if outcome == "win":
        if opponent_choice == "rock":
            my_choice = "paper"
        elif opponent_choice == "paper":
            my_choice = "scissors"
        else:
            my_choice = "rock"
    elif outcome == "lose":
        if opponent_choice == "rock":
            my_choice = "scissors"
        elif opponent_choice == "paper":
            my_choice = "rock"
        else:
            my_choice = "paper"
    else:
        my_choice = opponent_choice

    # Calculate Score
    # Draw
    if outcome == "draw":
        total_score += outcome_to_points["draw"] + choices_to_points[my_choice]
    # Win
    elif outcome == "win":
        total_score += outcome_to_points["win"] + choices_to_points[my_choice]
    # Lose
    else:
        total_score += outcome_to_points["lose"] + choices_to_points[my_choice]

print(total_score)
