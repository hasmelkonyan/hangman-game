import random

words = ["absurd", "buffalo", "crypt", "duplex", "dog", "elephant", "giraffe", "hurt", "ice", "cat", "lion", "monkey",
         "noisy", "opera", "purple", "lucky", "question", "rainbow", "sunglasses", "train", "umbrella", "violet",
         "wonder", "xylophone", "yellow", "zombie", "blue", "white", "dollar", "ball", "hurt", "animal", "love",
         "apple", "tangerine", "orange", "apricot", "tiger", "november", "birth", "flower", "mount", "insect",
         "sister", "girl", "friend"]
def get_word():
    word = random.choice(words)
    return word.lower()

def play(word):
    word_completion = "-" * len(word)
    print(f"there is {len(word)} letter {word_completion}")
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    word_letters = []
    print("Let's play")
    while not guessed and tries > 0:
        guess = input(" Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{guess}You already guess this letter!")
            elif guess not in word:
                print(f"{guess} - This letter not in word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job {guess} is in the word!")
                guessed_letters.append(guess)
                word_letters.append(guess)
                for i in range(len(word)):
                    if word[i] in word_letters:
                        print(word[i], end="")
                    else:
                        print("-", end="")
                if "-" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word")
            elif guess != word:
                print(f"{guess} is not the word")
                tries -= 1
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid guess!")
    if guessed:
        print("Congrats, you win!")
    else:
        print(f"Sorry, you have no more tries, you lose! the word was {word}")

def main():
    word = get_word()
    play(word)
    while input("You want play again? if yes, push '1'") == "1":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()






