#
#

import random

carbrands = ["ford","nissan","mustang","mercedes","porsche","bmw","fiat","volkswagen","audi","lamboghini","golf"]

random.shuffle(carbrands)

ans = list(carbrands[0])


#print (ans)


#empty list called show

show = []

# adds the variable answer to show
show.extend(ans)


#print(used)

#iterates through the list show

for i in range (len(show)):
    #replaces each index in the list with "_"
    show[i] = "_"

#the join command puts a space between each '_'
print (' '.join(show))
print()

#counter stops the game once all the letters have been guessed correctly
counter = 0
attempts = 5
#while loop to keep asking user until all letters have been guessed correctly

while counter < len(ans):
    guess = input("Please guess the word by guessing a letter: ")
    guess = guess.lower()
    print (counter)


    #iterates through the letters in the answer per index in the list
    for i in range(len(ans)):
        #if the guessed letter matches a letter in the answer ##then replace
        if ans[i] == guess :
    #then replace the index of that guessed word with the absolute guessed word
          show[i] = guess
          counter = counter + 1
          print("correct, keep guessing, you have ! ")

 
    #print out the new string with guessed letters in
    print (' '.join(show))
#    print()

print("Congratulations!, you've guessed the Word correctly")
