
file = ["- ? this is a sentence", "- ? this is another sentence"]

out = []
front = ""
back = ""
card_started = 0 # local variable in the function

#def handle(line):
    #if the line contains the delimiter, the front/back needs to be surrounded in quotes
    # if the line is surrounded by quotes and contains quotes, the in-card quotes needs to be double quoted

for line in file:
    if line[:4] == "- ? ": #if line starts with the newcard condition, new card found
        if card_started == 1:
            print("it's time to stop") # time to terminate the previous card
            out.append(front + "|" + back) # return the previous card
            front = "" # empty both values
            back = ""
        print("card found")
        front = line[4:] # store the question
        card_started = 1 
        continue
        # how to check the next line? 
    # if the line doesnt start with the question, it is either a continuation or an external point 
    elif line[:2] != "- " and card_started == 1: # it's not an external point, so its a continuation
        back + line + "<br>" # store the line. im not sure if the newline is stored but i dont think so
    # whats left is only external points which has to terminate the collection
    card_started = 0 #terminate collection
    out.append(front + "|" + back) # return card
    front = "" # empty the values
    back = ""
    continue


print(out.join("\n"))


#if line[:2] != "- ":
#    back = line
