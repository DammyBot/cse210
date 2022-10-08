import random

# Hilo game steps
"""
The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.
"""

def main():
    """
    The main part of the code that calls the classes and other parts of the code
    """
    current_card = Card.display_card()
    answer = "y"
    while Output.points > 0 and answer == "y":
        print(f"The card is {current_card}")
        previous_card = current_card
        current_card = Card.display_card()
        Output.options(previous_card, current_card)
        print(f"Your next card was: {current_card}")
        print(f"Your score is: {Output.points}")
        answer = ComputeResult.game_over()
    print("End")

class Card():
    # Picks a random card number between 1 and 13
    def display_card():
        picked_card = random.randint(1, 13)
        return picked_card

class Output():
    # Starting points
    points = 300

    # Calculating points
    def options(previous,current):
        try:
            option = input("Pick a card [h/l]: ").lower()
            if (option == "h") and current > previous:
                Output.points += 100
            elif (option == "h") and current < previous:
                Output.points -= 75
            if (option == "l") and current < previous:
                Output.points += 100
            if (option == "l") and current > previous:
                Output.points -= 75
        except TypeError as typeerror:
            print("Please enter a correct value")
        except ValueError as valueerror:
            print("Please enter a normal value")

        Output.points

class ComputeResult():
    
    def game_over():
        if Output.points > 0:
            answer_yes = input("Would you like to keep playing? [y/n]: ")
        else:
            answer_yes = "n"
            print("Game Over")
        return answer_yes

if __name__ == "__main__":
    main()