import pyinputplus as pyip
# debug inputs
#file = ["- ? this is a sentence", "  - this is an answer", "- stop", "- ? this is another sentence"]

# TODO: take in the file

# check to make sure this is a note that I really want to convert since it is one-way 
def confirm_conversion(file):
    yaml = 0
    print("confirming that the file is suitable for conversion")
    for line in file:             
        if line == "---" and yaml == 0:
            print("frontmatter start detected")
            yaml = 1
            continue
        if line == "notes_progress: complete":
            print("confirmation detected")
            return True
        if line == "---" and yaml == 1:
            print("frontmatter end detected")
            yaml = 0
            break
    print("file parsed. Confirmation not detected")
    manual_confirmation = pyip.inputYesNo("do you still want to parse the contents of this file? (y/n)\n", yesVal="y", noVal="n")
    if manual_confirmation == "y":
        print("confirmation detected")
        return True
    elif manual_confirmation == "n":
        print("termination detected. terminating...")
        return False

def handle(line):
    # TODO
    # if the line contains the delimiter, the front/back needs to be surrounded in quotes
    # if the line is surrounded by quotes and contains quotes, the in-card quotes needs to be double quoted
    return newline


# defining helper variables\
def parse_and_convert(file):
    out = []
    front = ""
    back = ""
    card_started = 0 # local variable in the function

    for line in file:
        if line[:4] == "- ? ": #if line starts with the newcard condition, new card found
            if card_started == 1:
                print("it's time to stop") # time to terminate the previous card
                out.append(front + "|" + back) # return the previous card
                front = "" # empty both values
                back = ""
            print("card found")
            front = handle(line[4:]) # store the question
            card_started = 1 
            continue
            # how to check the next line? 
        # if the line doesnt start with the question, it is either a continuation or an external point 
        elif line[:1] == "\t" and card_started == 1: # continuation definition is begin with a tab
            back + handle(line) + "<br>" # store the line, including the tab, and newline in html
        # whats left is only external points which has to terminate the collection. they should not be indented
        card_started = 0 #terminate collection
        out.append(front + "|" + back) # return card
        front = "" # empty the values
        back = ""
        continue

    out.append(front + "|" + back)

    return "\n".join(out) #returns the entire text 

if confirm_conversion(file):
    print(parse_and_convert(file))