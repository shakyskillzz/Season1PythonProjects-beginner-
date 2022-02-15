
print("Welcome to the quiz about me! ")
print("Answer 3 quick questions about me bc why not. ")
answerToPlay = input('''Type "yes" to start! ''')

if answerToPlay.lower() != 'yes':
    print("bakka")
    quit()
print("Lets go!")

score = 0

# question 1
print("Type only the letter of the answer choice you think is correct. ")
print("How many jobs have I had?")
print("a.) 3")
print("b.) 7")
print("c.) 5")
answer = input()

if answer.lower() == "b":
    score += 1
else:
    print("nani?")


# question 2
print("Who is my waifu?")
print("a.) konan")
print("b.) mai san (bunny girl)")
print("c.) zero-two(darling)")
answer = input()

if answer.lower() == "b":
    score += 1
else:
    print("nani?")

# question 3
print("Who is my favorite youtuber? ")
print("a.) Logan Paul")
print("b.) David dobrik")
print("c.) KSI")
answer = input()

if answer.lower() == "b":
    score += 1
else:
    print("nani?")

if score == 3:
    print("3/3 you know me too well :)")
else:
    print(f"{score}/3. The world shall know pain")




































