import numpy as np

class simple_game():
    def __init__(self):
        self.options = ["Rock", "Paper", "Scissors"]
        self.wins = 0

    def play(self, user_select):  
        computer_choice = np.random.choice(self.options)  # fresh move every time
        
        if user_select == computer_choice:
            print("Got it!")
            self.wins += 1
        else:
            print("Not it")
        
    
    

computer_play = simple_game()


def main():
        print("\n Let's play a game\n")
        print("You're to simply select 1, 2 or 3")
        print("we will play the game 7 times and you must have above 5 wins to call it a win")
        print()
        print("Ready? 1 for yes and 0 for no")

        choice1 = int(input("0 or 1"))
        if choice1 == 0:
            pass
        elif choice1 == 1:
            while True:

                print("\nLet's go!\n")
                print("I'm holding either of the below, make a guess by selecting the number\n")
                print("1. Rock")
                print("2. Scissors")
                print("3. Paper")


                trials = 3
                while trials > 0:
                    choice2 = int(input("What am i holding"))
                    if choice2 == 1:
                        choice2 = "Rock"
                    elif choice2 == 2:
                        choice2 = "Scissors"
                    elif choice2 == 3:
                        choice2 = "Paper"
                    else:
                        print("Invalid choice! Try again.")
                    computer_play.play(choice2)
                    print(f"Round {4 - trials}")
                    print(f"You have {trials - 1} trials left, so continue guessing" if trials > 1 else "last trial")

                    trials -=1

                print(f"You got {computer_play.wins}!")
                if computer_play.wins >= 2:
                    print("You won!\n")
                else:
                    print("It's a lost!\n")

                print("Do you want to play again? 1 for yes and 0 for no")
                choice3 = int(input("0 or 1"))
                if choice3 == 0:
                    print("Thanks for playing")
                    break
                elif choice3 == 1:
                    continue

             
        else:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()