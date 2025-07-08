import random
from colorama import Fore, Style, init
init(autoreset=True)

ran_num = random.randrange(1, 100)
win_streak = 0

while True:
    difficulty =input("""Pick easy medium or hard:
        🙄 easy (15 guesses)
        😜 medium (10 guesses)
        😈 hard(5 guesses) 
        """)
    
    if difficulty not in ["easy", "medium", "hard"]:
        print("please write easy medium or hard.")
        continue

    
    if difficulty == "easy":
        guesses = 15

    if difficulty == "medium":
        guesses = 10

    if difficulty =="hard":
        guesses = 5

    counter = 0
    for i in range(guesses):
        guess = int(input("Lets test your luck! Pick a number its only from 1 to 100! "))
        if guess > ran_num:
            counter +=1
            print(Fore.RED +"Too High!😬")
        elif guess < ran_num:
            counter +=1
            print(Fore.RED +"Too Low!😬")
        else:
            win_streak += 1
            print(Fore.GREEN + f"🎯 Well done you bloody did it! You have a win streak of {win_streak}")
            break

        if guesses == counter:
            win_streak == 0
            print(Fore.RED + "You Lose!")
            break

    play_again = input("play again? y/n ")
    if play_again != "y":
        print("Thanks for playing!🏁")
        break