import random
fiveword=["fruit","horse","mouse","ratio","mends","lucky","eagle","chief","snake","earth","stack","ports","exits","dates","enter","shift"]
word=random.choice(fiveword)
board=[["_","_","_","_","_"],
       ["_","_","_","_","_"],
       ["_","_","_","_","_"],
       ["_","_","_","_","_"],
       ["_","_","_","_","_"],
       ["_","_","_","_","_"]]
for y in range(0,6):
    for x in board:
        print(x)
    i=0
    while(i==0):
        guess=input("what is your guess")
        if len(guess) ==5: #if it is a valid guess
            i=1
            index=0
            guess=guess.lower()
            if guess!=word:
                for j in guess:
                    try:
                        if guess.index(j)==word.index(j): #green
                            j=j.upper()
                            board[y][index]=j
                            index+=1
                        else:
                            board[y][index]=j+"*"
                            index+=1#yelloow
                    except:
                        board[y][index]=j
                        index+=1 #gray
            else:
                
                for x in board:
                    print(x)
                print("you won")
                quit()
        else:
            print("try again")
for x in board:
   print(x)
print("you lost, the word was,", word)