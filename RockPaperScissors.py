import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["Rock", "Paper", "Scissors"]
        self.player_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Scissors" and computer_choice == "Paper") or \
             (player_choice == "Paper" and computer_choice == "Rock"):
            self.player_score += 1
            return "Congratulations! You win!"
        else:
            self.computer_score += 1
            return "Sorry, you lose! Try again."

    def play(self):
        print("Welcome to Rock, Paper, Scissors!")
        while True:
            player_choice = input("Choose: Rock, Paper, or Scissors (or type Exit to quit): ").strip().capitalize()
            if player_choice == "Exit":
                print("Thanks for playing! See you next time!")
                print(f"Final Score - Player: {self.player_score}, Computer: {self.computer_score}")
                break
            if player_choice not in self.choices:
                print("Invalid choice. Please try again.")
                continue
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            result = self.determine_winner(player_choice, computer_choice)
            print(result)
            print(f"Score - Player: {self.player_score}, Computer: {self.computer_score}")
            print()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()
