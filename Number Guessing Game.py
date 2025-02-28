import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        # Step 1: Define the range of numbers
        lower_bound = 1
        upper_bound = 100
        print(f"I have selected a number between {lower_bound} and {upper_bound}.")

        # Step 2: Generate a random number
        target_number = random.randint(lower_bound, upper_bound)

        # Step 5: Initialize the attempts counter
        attempts = 0
        guessed_correctly = False

        # Step 4: Use a loop for multiple attempts
        while not guessed_correctly:
            # Step 3: Take player input
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment the attempts counter

            # Step 4: Compare player guess to target number
            if guess < target_number:
                print("Too low, try again!")
            elif guess > target_number:
                print("Too high, try again!")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
                guessed_correctly = True  # Exit the loop

        # Step 7: Allow the player to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break  # Exit the main loop

# Run the game
number_guessing_game()
