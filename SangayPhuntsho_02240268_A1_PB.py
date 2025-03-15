import random

def guess_number_game():
    min_num = 1
    max_num = 15
    secret_number = random.randint(min_num, max_num)
    print(f"Guess a Number:")
    print(f"The number should be between {min_num} and {max_num}.")
    
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        try:
            user_guess = int(input("Guess a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        if user_guess == secret_number:
            print(f"Congratulations! You have guessed the correct number {secret_number} in {attempts} attempts!")
            guessed_correctly = True
        elif user_guess > secret_number:
            print("Too High!... Try again.")
        else:
            print("Too Low!... Try again.")

def rock_paper_scissors():
    print("Choose the following option (1-3).")
    print("1. Rock\n2. Paper\n3. Scissors")
    
    attempts = 0
    while True:
        choices = ["Rock", "Paper", "Scissors"]
        computer = random.choice(choices)
        user_input = input("Enter one of the above options: ").capitalize() 
        # Accepts 'rock', 'Rock', etc.
        if user_input not in choices:
            print("Invalid option, try again.")
            continue
        
        attempts += 1
        print(f"Computer choice is {computer}")
        
        if user_input == computer:
            print("It's a tie!")
        elif (user_input == "Rock" and computer == "Scissors") or (user_input == "Paper" and computer == "Rock") or (user_input == "Scissors" and computer == "Paper"):
            print("Yes! You won!")
        else:
            print("Sorry, you lose.")

def game_selection():
    print("Hello, welcome to my game")
    print("Select function 1 to 3")
    print("1. Guess the number\n2. Rock, Paper, Scissors game\n3. Exit game")
    
    try:
        game = int(input("Enter the number: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    if game == 1:
        print("You have selected Guess the Number game")
        guess_number_game()
    
    elif game == 2:
        print("You have selected Rock, Paper, Scissors game")
        rock_paper_scissors()
    
    elif game == 3:  
        print("Exit program")
        return
    
    else:
        print("Please use a valid option.")

if __name__ == "__main__":
    game_selection()