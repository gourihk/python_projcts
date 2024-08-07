import random

top_of_range = input("type a number to guess within limit:  ")

#check if input is digit and convert it to int
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("please type a number greater than 0")
        quit()

else: 
    print("please type a number")


random_number = random.randint(0,top_of_range)

#check until they guess the number
guess_no = 0

while True:
    guess_no += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
       guess=int(guess)
    else:
        print("Please Type a number next time")
        continue

    if guess == random_number:
        print("Correct guess")
        break
    else:
        print("incorrect guess")

#how many guesses does the user take
print(" you got it in ", guess_no , 'guesses')
    
