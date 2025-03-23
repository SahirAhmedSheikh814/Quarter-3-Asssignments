import random
import string
from words import words
from hangman_visual import lives_visual_dict

def get_valid_word(words):
    """Randomly selects a valid word from the list (avoiding spaces & hyphens)."""
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    """Main function for the Hangman game."""
    print("\n🎩 Welcome to Hangman! Guess the word before you run out of lives. 🎯")
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # What the user has guessed
    lives = 7

    # Asking user if they want a hint (optional)
    hint_choice = input("\nWould you like a hint? (yes/no): ").strip().lower()
    if hint_choice in ["yes", "y"]:
        print(f"💡 Hint: The word starts with '{word[0]}'.")

    while len(word_letters) > 0 and lives > 0:
        # Display game status
        print("\n-----------------------------------")
        print(f"❤️ Lives left: {lives}")
        print(f"🔠 Used letters: {' '.join(sorted(used_letters)) if used_letters else 'None'}")
        print(lives_visual_dict[lives])  # Display hangman visual

        # Display current guessed word
        word_display = [letter if letter in used_letters else '-' for letter in word]
        print(f"📝 Word: {' '.join(word_display)}")

        # Get user input
        user_letter = input("\n🔡 Guess a letter: ").strip().upper()

        # Input validation
        if len(user_letter) != 1 or user_letter not in alphabet:
            print("❌ Invalid input! Please enter a single valid letter.")
            continue
        if user_letter in used_letters:
            print("⚠️ You've already guessed this letter. Try another one.")
            continue

        # Update guessed letters
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print("✅ Correct guess!")
        else:
            lives -= 1
            print(f"❌ Wrong guess! '{user_letter}' is not in the word.")

    # Game over conditions
    print("\n-----------------------------------")
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"💀 You lost! The word was: {word}")
    else:
        print(f"🎉 Congrats! You guessed the word: {word} 🎊")

    # Ask if the user wants to play again
    play_again = input("\n🔄 Would you like to play again? (yes/no): ").strip().lower()
    if play_again in ["yes", "y"]:
        hangman()
    else:
        print("\nThanks for playing! See you next time. 😊")

# Run the game
if __name__ == "__main__":
    hangman()
