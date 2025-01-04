import random
from logo import logoo

stages = [
"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___
""",
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
    """
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """
]
word_list = ["messi","neymar","pedri","gavi"]
print(logoo)
lives = 6
chosen_word = random.choice(word_list)
#print(chosen_word)
placeholder= ""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_"
print(placeholder)
game_over = False
correct_letters = []
while not game_over:
    print(f"********************{lives}/6 LIVES LEFT************************")
    guess = input("Guess the footballer names: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a Life. ")
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE****************")
    if "_" not in display:
        game_over = True
        print("*********************YOU WIN********************* ")
    print(f" length of stages{len(stages)}")
    print(f"lives {lives}")
    print(stages[lives])
