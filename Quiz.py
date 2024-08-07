print("welcome to my computer quiz")

#ask if the user wants to play the game or not
playing = input("Do you want to play? ")

#check if they said yes
if playing.lower() != "yes":
    quit()

print("Okay! lets play: ")

#keep scores 
score = 0

#Q1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score +=1
else:
    print("Incorrect!")

#Q2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score +=1
else:
    print("Incorrect!")

#Q3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score +=1
else:
    print("Incorrect!")

#Q4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('correct!')
    score +=1
else:
    print("Incorrect!")

print("You got " +str(score) + " quetions correct!")