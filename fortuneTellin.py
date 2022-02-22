import random

food_choice = ['soup', 'salad', 'steak', 'pizza', 'chicken', 'pasta', 'fancy restraunt', 'fast food', 'hamburgers']

num_kids = random.randint(0,7)
age_married = random.randint(23,60)
food = random.choice(food_choice)



fortune_kids = True
fortune_marry = True
fortune_food = True
finished = False

def display_message():
    print("What would you like to know?")
    print("a.) How many kids will I have in my life? ")
    print("b.) At what age will I get married?")
    print("c.) What will I be eating tomorrow?")
    print("type only the letter of which ever one or 'q' to quit.")

def display_message2():
    print("What else would you like to know?")
    print("a.) How many kids will I have in my life? ")
    print("b.) At what age will I get married?")
    print("c.) What will I be eating tomorrow?")
    print("type only the letter of which ever one or 'q' to quit.")


while finished == False:

    print("Would you like your fortune to be told?")
    print('''Type "yes" or "no"''')
    answer_to_play = input().lower()
    
    if answer_to_play == "yes":
        print("Ok lets do it!")
        while True:

            if fortune_food == True and fortune_kids == True and fortune_marry == True:
                display_message()
                user_answer = input().lower()
                if user_answer == "a":
                    print(f"you will have {num_kids} kids when your older.")
                    fortune_kids = False
                elif user_answer == "b":
                    print(f"you will get married at {age_married} year old.")
                    fortune_marry = False
                elif user_answer == "c":
                    print(f"You will be eating {food} tomorrow.")
                    fortune_food = False
                elif user_answer == "q":
                    finished = True
                    break
                else: 
                    print("Thats not one of the choices dude try again.")


            if fortune_food == False and fortune_kids == True and fortune_marry == True:
                display_message2()
                user_answer = input().lower()
                if user_answer == "a":
                    print(f"you will have {num_kids} kids when your older.")
                    fortune_kids = False
                elif user_answer == "b":
                    print(f"you will get married at {age_married} year old.")
                    fortune_marry = False
                elif user_answer == "c":
                    print("You already chose that one dude try another one.")
                elif user_answer == "q":
                    finished = True
                    break    
                else: 
                    print("Thats not one of the choices dude try again.")


            if fortune_food == True and fortune_kids == False and fortune_marry == True:
                display_message2()
                user_answer = input().lower()
                if user_answer == "a":
                    print("you already chose this one dude try another one")
                    
                elif user_answer == "b":
                    print(f"you will get married at {age_married} year old.")
                    fortune_marry = False
                elif user_answer == "c":
                    print(f"You will be eating {food} tomorrow.")
                    fortune_food = False
                elif user_answer == "q":
                    finished = True
                    break
                else: 
                    print("Thats not one of the choices dude try again.")


            if fortune_food == True and fortune_kids == True and fortune_marry == False:
                display_message2()
                user_answer = input().lower()
                if user_answer == "a":
                    print(f"you will have {num_kids} kids when your older")
                    fortune_kids = False
                elif user_answer == "b":
                    print(f"you already chose this one dude try another one")
                    
                elif user_answer == "c":
                    print(f"You will be eating {food} tomorrow.")
                    fortune_food = False
                elif user_answer == "q":
                    finished = True
                    break
                else: 
                    print("Thats not one of the choices dude try again.")


            if fortune_food == False and fortune_kids == False and fortune_marry == True:
                display_message2()
                user_answer = input().lower()
                if user_answer == "a":
                    print("You already chose this one dude try again")
                    
                elif user_answer == "b":
                    print(f"you will get married at {age_married} years old")
                    fortune_marry = False
                elif user_answer == "c":
                    print("You already chose this one dude try again")
                elif user_answer == "q":
                    finished = True
                    break    
                else: 
                    print("Thats not one of the choices dude try again.")
        

            if fortune_food == True and fortune_kids == False and fortune_marry == False:
                display_message2()
                user_answer = input().lower()
                if user_answer == "a":
                    print("you already chose this one dude try again")
                    
                elif user_answer == "b":
                    print(f"you already chose this one dude try another one")
                    
                elif user_answer == "c":
                    print(f"You will be eating {food} tomorrow.")
                    fortune_food = False
                elif user_answer == "q":
                    finished = True
                    break
                else: 
                    print("Thats not one of the choices dude try again.")


            if fortune_food == False and fortune_kids == True and fortune_marry == False:
                display_message2()
                user_answer = input().lower()
                if user_answer == "a":
                    print(f"you will have {num_kids} kids when your older")
                    fortune_kids = False
                elif user_answer == "b":
                    print("you already chose this one dude try another one")
                    
                elif user_answer == "c":
                    print("You already chose this one dude try another")
                elif user_answer == "q":
                    finished = True
                    break
                else: 
                    print("Thats not one of the choices dude try again.")


            if fortune_food == False and fortune_kids == False and fortune_marry == False:
                print("Your fortune has been told.")
                finished = True
                break






    elif answer_to_play == "no":
        print("So be it..")
        break

    else:
        print("Sorry didnt understand you. try again")
        continue

print("byeeee")

