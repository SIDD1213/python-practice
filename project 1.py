import random

def number_guessing_game():
    secret = random.randint(1, 100)
    attempts = 0

    print("Guess a number between 1 and 100!")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break
if __name__ == "__main__":
    number_guessing_game()