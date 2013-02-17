high = 100
low  = 0
guess= (high+low)/2
line = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "

print("Please think of a number between 0 and 100!")
print("Is your secret number "+ str(guess) + "?")

enter=raw_input(line)

while enter!='c':
    if enter !='h'  and enter !='l':
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(guess)+ "?")
        enter=raw_input(line)
    elif enter=='h':
        high = guess
        guess = (low + guess)/2
        print("Is your secret number " + str(guess)+ "?")
        enter=raw_input(line)
    elif enter=='l':
        low = guess
        guess = (high+ guess)/2
        print("Is your secret number " + str(guess)+ "?")
        enter=raw_input(line)
        
print('Game over. Your secret number was: ' + str(guess))
