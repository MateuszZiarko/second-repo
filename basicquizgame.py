def new_game():

    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in questions:
        print("----------------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess) 

        correct_guesses += check_answer(questions.get(key),guess)
        question_number += 1 
    display_score(correct_guesses, guesses)

#----------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
#----------------------------
def display_score(correct_guesses, guesses):
    print("----------------------------")
    print("Results:")
    print("----------------------------")
    print("Answers:", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses:", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
#----------------------------
def play_again():

    response = input("Do you want to play again? (yes or no):").upper()

    if response == "YES":
        return True
    else:
        return False

#----------------------------
questions = {"In which year was League Of Legends launched?": "A",
             "How many champions are there in the game?": "A",
             "What does Tristana carry in her pocket?": "B",
             "How popular is League Of Legends?": "C",
             "Who killed Vayne's parents?": "D",
             "How much gold do you start with in a Summoner's Rift match?": "C",
             "Which champion is Garen’s sibling?": "B",
             "Who created Blitzcrank?": "A",
             "How was the 3vs3 map called?": "B",
             "How many champions were available when the game was released?": "B",}


options = [["A. 2009", "B. 2011", "C. 2007", "D. 2008"],
           ["A. 140", "B. 145", "C. 135", "D. 130"],
           ["A. A pocket", "B. A rocket", "C. A chair", "D. A gun"],
           ["A. It is the most popular games in the e-sport industry", "B. Not popular at all", "C. It is one of the most popular games in the e-sport industry", "D. Sort of popular"],
           ["A. Lux", "B. Warwick", "C. Corki", "D. Evelynn"],
           ["A. 350", "B. 400", "C. 500", "D. 600"],
           ["A. Corki", "B. Lux", "C. Sion", "D. Lucian"],
           ["A. Viktor", "B. Garen", "C. Dr.Mundo", "D. Nunu"],
           ["A. Dark Forest", "B. Twisted Treeline", "C. Forbidden Forest", "D. Forsaken Forest"],
           ["A. 50", "B. 40", "C. 30", "D. 25"],]

new_game()

while play_again():
    new_game()

print("Bye!\nHave a great day!")