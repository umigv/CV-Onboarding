import random

class Hangman:
    def __init__(self, word_list, max_incorrect=6):
        self.word = random.choice(word_list).lower()
        self.guessed = set()
        self.max_incorrect = max_incorrect
        self.guesses = 0
        self.display = ['_' for letter in self.word]
    
    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed:
            return f"You have already guessed the letter '{letter}', try again."
        else:
            self.guessed.add(letter)
        if letter in self.word:
            for index, l in enumerate(self.word):
                if l == letter:
                    self.display[index] = l
            return "Correct guess!"
        else:
            self.guesses += 1
            return f"Wrong! You have {self.max_incorrect - self.guesses} guesses left."
    
    def won(self):
        return '_' not in self.display

    def lost(self):
        return self.guesses >= self.max_incorrect

    def get_display(self):
        return ' '.join(self.display) #put spacebetween underscore for better readability and also helps return an output for display

    def get_word(self):
        return self.word   

game = Hangman(['python', 'machinelearning', 'arv']) #word list for guessing
print("Welcome to Hangman! You have 6 guesses.")
print("Guess the word: ", game.get_display())
while not game.won() and not game.lost():
    letter = input("Guess a letter: ")
    result = game.guess(letter)
    print(result)
    print("Word:", game.get_display())
    print()
if game.won():
    print("Good job! You guessed correctly:", game.get_word())
else:
    print("Sorry, you lost. The word was:", game.get_word())
