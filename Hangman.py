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
words = input("enter a word or sentence without punctuation: ")
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
        print("".join(gameboard))
        return True
    else:
        print("Incorrect Gueess Try Again!")
        print(counter)
        return False

counter = 0
win = True
while counter < 10:
    guessed_correct = guess(counter)#user is asked to guess a letter
    if guessed_correct:
        if "_" in gameboard: ##if underscores left, guess again
            continue
        else:                   ###if no underscore left, then they won
            print("You Win!")
            exit()###if no underscore left, then they won
    else:
        if counter < 10: ###if there is anymore strikes left
            counter += 1
            continue ###guess again
        else:           ###else if not anymore strikes left, game over
            print("Game Over!")
            exit()



#the game starts with zero guesses 
#the user hasn't won yet
#user is asked to input a word or phrase
#replace word or phrase with underscores
#underscores get printed
#user is asked to guess a letter
#check if the guess is correct
#if yes, replace underscore with same index as the value of guess - if no, ask the user to input new guess
#if user guesses word in under 10 guesses, stop the game and tell user they won
#if user has made 10 guesses and not guessed the word, stop game and telk user they lost