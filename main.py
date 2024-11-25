logo = """
 ______              _                     ______                       
|  ___ \            | |                   / _____)                      
| |   | |_   _ ____ | | _   ____  ____   | /  ___ _   _  ____  ___  ___ 
| |   | | | | |    \| || \ / _  )/ ___)  | | (___) | | |/ _  )/___)/___)
| |   | | |_| | | | | |_) | (/ /| |      | \____/| |_| ( (/ /|___ |___ |
|_|   |_|\____|_|_|_|____/ \____)_|       \_____/ \____|\____|___/(___/ 
                                                                        
"""




import random
num = random.randint(1,100)
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100")
level = input("Choose a difficulty, type 'easy' or 'hard': ")
if level=="easy":
    attempt=10
else:
    attempt=5

program_run=True

while attempt!=0 and program_run:
    print(f"\nYou have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess<num:
        print("\nToo Low.")
        attempt-=1
        print("Guess again.")
    elif guess>num:
        print("\nToo high.")
        attempt-=1
        print("Guess again.")
    elif guess==num:
        print(f"\nYou got it! The answer was {num}.")
        program_run=False

if attempt==0:
    print("\nYou ran out of attempts, you lost!")

