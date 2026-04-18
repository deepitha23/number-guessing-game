import random

print("🔥 Are you ready, math genius?")
print("I got you 😎 Let's begin!\n")

N = random.randint(1, 100)
attempts = 0
max_attempts = 15

name = input("Enter your name: ")

while attempts < max_attempts:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    print("Attempts left:", max_attempts - attempts)

    if guess > N + 10:
        print("Too high!")

    elif guess > N:
        print("High")

    elif guess < N - 10:
        print("Too low!")

    elif guess < N:
        print("Low")

    else:
        print("🎉 Correct!")
        print(f"Good job, {name} 😄")
        print("You guessed it in", attempts, "attempts")
        break

# If user fails
if attempts == max_attempts and guess != N:
    print("😢 Game Over!")
    print("The number was:", N)
    print("I got you... try again, you’ll win next time 💪")
