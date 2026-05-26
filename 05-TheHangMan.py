import random

Word_List = ["seal", "fatrat", "pig"]
Chosen_word = random.choice(Word_List)

Display = ""
for letter in Chosen_word:
    Display += "_"

Game_Over = False
Correct_Letters = []

while not Game_Over:
    Guess = input("Guess a letter: ").lower()
    
    if Guess in Chosen_word:
        Correct_Letters.append(Guess)
    
    Display = ""
    for Letter in Chosen_word:
        if Letter.lower() in Correct_Letters:
            Display += Letter
        else:
            Display += "_"
    
    print(Display)
    
    if "_" not in Display:
        Game_Over = True
        print("You Win!")