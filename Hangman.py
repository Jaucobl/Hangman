#Create the gallow that the man would be hanged upon
#Be able to end the game if the word is guessed correctly
print("----------")
print("|        |")
print("|        |")
print("|")
print("|")
print("|")
print("-----------")
#First we would ask the user for a word that is going to be guessed
words = input("enter a word or sentence without punctuation")
#Create the variable that the word would be stored in
#Clear the word off of the screen
gameboard = []
for each in list(words):
    if each != " ":
        gameboard.append("_")
    else:
        gameboard.append(" ")
show = ""
for each in gameboard:
    show += each

print(show)

#Take the length of the word and create a number of underscores equal to it
## Figure out how to output the underscore and spaces correctly
#If there are spaces in users input, keep them as spaces
#Then we would ask another user for a letter guess

def guess(counter):
    letter = input("Enter a one letter gues: ")
    counter += 1
    if letter in list(words):
        for idx, value in enumerate(list(words)):
            if letter == value:
                gameboard[idx] = value
        print(gameboard)
    else:
        print("Incorrect Gueess Try Again!")

counter = 0
while counter < 10:
    guess(counter)


print("Game Over")



#If the letter is in the word, put the letter in its original position
#Repeat asking the user for a letter #If they succeed, then display a you won screen and then offer an option to restartuntil the user runs out of guesses or the word is guessed
#If they fail then after the hangman dies, display a game over screen and then offer an option to restart
