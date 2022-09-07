# flashcards.py
from array import array
import json
from tkinter import N, Y

with open('me-capitals.json', 'r') as f:
    data = json.load(f)


total = len(data["cards"])
score = 0
#This will tally the score as the player answers the questions

y = Y
n = N
# These will allow the player to play or quit the game from the start

print()
username = input("Howdy! I'm AI Trebek. What's your name?: ")
print()

print(f"Welcome {username}! Let's test your knowledge on Middle Eastern countries capitals!")

print() #Added to provide space between strings.

ready_player = input("Are you ready to play? Y/N?")
if ready_player.lower() == y.lower():

    print()  #Added to provide space between strings.

    print(f"Ok {username}! Let's play!")
if ready_player.lower() == n.lower():

# I added a start of game message using f-string.
# The player can enter their name and anwser if they are ready to play.

    print()  #Added to provide space between strings.

    print("Ok, fine bye Felicia!")
    print()
    quit()

print()  #Added to provide space between strings.

for i in data["cards"]:
   
    guess = input(i["q"] + " > ")

    if guess.lower()== i["a"].lower():
        # increment score up one
        score += 1
        # interpolate score and total into the response
        print()
        print(f"Correct! Current score: {score}/{total}")
    
    else:
        print() #Added to provide space between strings.

        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")

        print()  #Added to provide space between strings.

 #added the "end" variable with the len()  and interpolated username, score and total   

end = len(data["cards"])

#printed using f-string to display the end message containing the score/total.  
print(f"Thanks for playing {username}! You scored: {score}/{total}")
    
half_correct = total / 2
if score == total:
    print("You are the champion! ")
elif score == 0:
    print("Oof, maybe try again! ")
elif score > half_correct:
    print("Noice!")
elif score < half_correct:
    print("You might want to try again! ")
print() #Added to provide space between strings.
