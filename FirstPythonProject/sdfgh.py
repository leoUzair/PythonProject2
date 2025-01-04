import random
stages = [''' 
"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___ ,
"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    """,
"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    """,
"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    """,
"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    """,
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """
''']

def display(word, guessed_letters):
    return "".join([letter if letter in guessed_letters else "_" for letter in word])


def hangman():
    # List of words to choose from
    word_list = ["python", "javascript", "hangman", "programming", "computer"]

    # Randomly choose a word
    word = random.choice(word_list)

    guessed_letters = set()  # To track guessed letters
    attempts = 6  # Number of attempts before game over
    guessed_word = display(word, guessed_letters)

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while attempts > 0:
        print(f"\nWord: {guessed_word}")
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        # Get user input
        guess = input("Guess a letter: ").lower()

        # Check if the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try another one.")
            continue

        guessed_letters.add(guess)

        # If the letter is in the word, update the guessed word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

        guessed_word = display(word, guessed_letters)

        # Check if the word is guessed correctly
        if guessed_word == word:
            print(f"\nCongratulations! You've guessed the word: {word}")
            break


    else:
        print(f"\nGame over! The word was: {word}")




if __name__ == "__main__":
    hangman()
