from random import randint
guesses = [0,0]

def flipcoin():
    return randint(0,1)

def playgame():
    flip1 = flipcoin()
    flip2 = flipcoin()
    if flip1 | flip2 == True:
        if flip1 & flip2 == True:
            guesses[0] += 1
        else:
            guesses[1] += 1

for x in range(1000):
    playgame()
    print(f"{x}: right {guesses[0]} wrong {guesses[1]}")

print(f"probability is {(guesses[0]/(guesses[0]+guesses[1]))*100}%")