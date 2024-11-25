# Number Guessing Game

## Overview
The **Number Guessing Game** is a fun, interactive Python-based game where players attempt to guess a randomly generated number between 1 and 100. The game provides feedback after each guess and allows the player to choose a difficulty level to adjust the number of attempts.

---

## Features
- **Random Number Generation**: A random number between 1 and 100 is generated for each game.
- **Difficulty Levels**:
  - **Easy**: 10 attempts.
  - **Hard**: 5 attempts.
- **Interactive Feedback**:
  - Feedback on whether the guess is too high, too low, or correct.
  - Remaining attempts displayed after each guess.
- **Win/Loss Conditions**:
  - Win if the correct number is guessed.
  - Lose if attempts run out.
- **Replay Option**: Encourages the player to start a new game after completing one.

---

## Requirements
- **Python 3.x**: Ensure Python is installed on your system.
- No external libraries are required.

---

## How to Play
1. Clone or download this repository to your local machine.
2. Open the project in your preferred Python IDE or text editor.
3. Run the script in a terminal or IDE.
4. Follow the on-screen prompts to play.

### Gameplay Instructions
- The program will randomly generate a number between 1 and 100.
- You can choose a difficulty level:
  - **Easy**: 10 attempts to guess the number.
  - **Hard**: 5 attempts to guess the number.
- Enter your guess when prompted.
- The program will provide feedback:
  - **Too low**: Your guess is lower than the target number.
  - **Too high**: Your guess is higher than the target number.
  - **Correct**: You guessed the number correctly!
- The game ends when:
  - You guess the correct number.
  - You run out of attempts.

---

## Example Gameplay
```
 ______              _                     ______                        
|  ___ \            | |                   / _____)                      
| |   | |_   _ ____ | | _   ____  ____   | /  ___ _   _  ____  ___  ___
| |   | | | | |    \| || \ / _  )/ ___)  | | (___) | | |/ _  )/___)/___)
| |   | | |_| | | | | |_) | (/ /| |      | \____/| |_| ( (/ /|___ |___ |
|_|   |_|\____|_|_|_|____/ \____)_|       \_____/ \____|\____|___/(___/
                                                                        

Welcome to the number guessing game!
I'm thinking of a number between 1 to 100.
Choose a difficulty, type 'easy' or 'hard': easy

You have 10 attempts remaining to guess the number.
Make a guess: 50

Too Low.
Guess again.

You have 9 attempts remaining to guess the number.
Make a guess: 75

Too high.
Guess again.

You have 8 attempts remaining to guess the number.
Make a guess: 63

You got it! The answer was 63.
```

---

## Code Explanation
### Key Functions
1. **Random Number Generation**:
   - The `random.randint(1, 100)` function generates a random number.
2. **Feedback**:
   - Conditional statements (`if`, `elif`, `else`) provide feedback to the player after each guess.
3. **Attempts Management**:
   - The remaining attempts decrease after each incorrect guess.
4. **Difficulty Levels**:
   - `Easy`: 10 attempts.
   - `Hard`: 5 attempts.
5. **Win/Loss Conditions**:
   - The game ends when the player guesses the correct number or runs out of attempts.

---

## Contributing
If you'd like to contribute to this project:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## Acknowledgments
- ASCII art enhances the visual presentation of the game.
- Inspired by classic number guessing games.

