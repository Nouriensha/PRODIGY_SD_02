import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

if __name__ == "__main__":
    guess_the_number()
