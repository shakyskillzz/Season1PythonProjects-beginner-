import random



def guessing_game(x):
    
    
    while True:
        score = 0
        guesses = 3

        print('''Do you want to guess? "yes" to play or "no" to stop. ''')
        user_answer = input("")
        if user_answer.lower() == "yes":
            while guesses > 0:

                number = random.randint(1,x)
                number_guess = int(input(f"Guess a number 1-{x}: "))


                if number == number_guess:

                    print(f"Noice you guessed {number} correctly")
                    score += 1
                    

                elif number != number_guess : 
                    print(f"cmon dude it was {number}")
                    guesses -= 1

            print(f"You guessed correctly {score} time(s).")
        if user_answer.lower() == "no":
            break

    

guessing_game(10)

print("Arigato!")
