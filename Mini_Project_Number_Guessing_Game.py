import random

secret_number = random.randint(1, 10)
attempts = 3

print("I am thinking of a number between 1 and 10.")

while attempts > 0:
    guess = int(input("Take a guess: "))
    if guess == secret_number:
        print("🎉 Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("📉 Too low! Try again.")
    else:
        print("📈 Too high! Try again.")
    attempts -= 1

if attempts == 0:
    print(f"😔 Sorry, you've run out of attempts. The secret number was {secret_number}.")