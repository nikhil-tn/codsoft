import random

def guess_number_game():
    print("Welcome to the Number Guessing Game!")
    play_again = True
    score = 0
    
    while play_again:
    
        number_to_guess = random.randint(1, 100)
        attempts = 0
        guessed_correctly = False
        max_attempts = 5  
        
        print(f"\nRound {score + 1}. Guess the number between 1 and 100!")
        
        while attempts < max_attempts and not guessed_correctly:
            try:
                user_guess = int(input("Enter your guess: "))
                
            
                if user_guess < number_to_guess:
                    print("Too low! Try a higher number.")
                elif user_guess > number_to_guess:
                    print("Too high! Try a lower number.")
                else:
                    print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
                    guessed_correctly = True
            except ValueError:
                print("Invalid input! Please enter a valid number.")
            
            attempts += 1
        
        if not guessed_correctly:
            print(f"\nSorry, you've run out of attempts. The number was {number_to_guess}.")
        
        score += 1 if guessed_correctly else 0
        
        play_again_input = input("\nDo you want to play again? (yes/no): ").lower()
        play_again = play_again_input == "yes"
    
    print(f"\nGame Over! Your final score is {score}.")


guess_number_game()
