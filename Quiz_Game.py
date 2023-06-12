# Ask user questions 
# correcct answer give 1 point
print("Welcome to Quiz")

playing = input("Do you want to play .? \n")

if playing != "yes":
    print("Okay See You")
    quit()
print("Okay! Let's play :-)")
score = 0


answer = input("What does CPU stands for.? \n")
if answer.lower() == "central processing unit":
    print("You are correct!")
    score += 1
else:
    print("Incorrect answer\n")

answer = input("What does RAM stands for.? \n")
if answer.lower() == "random access memory":
    print("You are correct!")
    score += 1
else:
    print("Incorrect answer\n")

answer = input("What does GPU stands for.? \n")
if answer.lower() == "graphics processing unit":
    print("You are correct!")
    score += 1
else:
    print("Incorrect answer\n")

answer = input("What does ROM stands for.? \n")
if answer.lower() == "read only memory":
    print("You are correct! \n")
    score += 1
else:
    print("Incorrect answer\n")

print("You got " + str(score) + " questions answered correctly\n")
print("Your correct answer percentage is " + str((score /4) * 100) + "%")


