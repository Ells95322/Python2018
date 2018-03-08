import random #You have to imprt this to use random Number on line 2 
randomNumber = random.randrange(1,10) #This is to get the random number
print("Random number has been generated") #This tells you when your number has been genarated

guessed = False #this sets guessed to fales
while guessed==False:  #this will loop untill guessed is true
    userInput = int(input("Your guess pleas: ")) #thsi asks for imput of a number
    if userInput==randomNumber: #this sees if user imput is the same as the random number
        guessed = True #if user imput is the same as the random number witch is checked
        #in the sataement on line 8 then set guessed to true
        print("Well done!")#after it sets guessed to true then print our well done
    elif userInput>10: #if the user imput is more than the highest number witch is 10 
    #then run the next line
        print("Our guess range is between 1 and 10, please try a bit lower") #prints that the 
        #guess is above the range of numbers set
    elif userInput<1: #if the user imput is less the the lowest number witch is 1 run the next line
        print("Our guess range is between 1 and 10, please try a bit higher") # prints that 
        #the guess is below the numbers set
    elif userInput>randomNumber: #checks waht the random number and the user imput and if user 
        #imput is grater than random nymber then run the next line
        print("Try one more time, a bit lower") #prints to guess lower
    elif userInput < randomNumber: #checks waht the random number and the user imput and if user 
        #imput is less than random nymber then run the next line
        print("Try one more time, a bit higher") #prints to guess higher
