import random

number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Welcome to the Number Guessing Game! 🎮")
print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")


while attempts < max_attempts:
    
    try:
        guess = int(input("\nGuess the number (between 1 and 100): "))
        attempts += 1
        
        # Check the guess against the random number
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100!")
            
            attempts -= 1
        elif guess < number_to_guess:
            print("Too low! Try again.")
            print(f"Attempts remaining: {max_attempts - attempts}")
        elif guess > number_to_guess:
            print("Too high! Try again.")
            print(f"Attempts remaining: {max_attempts - attempts}")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} {'attempt' if attempts == 1 else 'attempts'}!")
            break
            
    except ValueError:
        print("Please enter a valid number!")
        attempts -= 1

if attempts >= max_attempts and guess != number_to_guess:
    print(f"\nGame over! Better luck next time! The number was {number_to_guess}. ")
    
print("\nThanks for playing! ")