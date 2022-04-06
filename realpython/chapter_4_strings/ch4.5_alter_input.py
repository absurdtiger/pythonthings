### 4.5 Pick Apart your user's input ###

# this program is totally called first_letter.py

question = "TELL ME SOMETHING "
they_said = input(question)
THEY_SAID = they_said.upper()
print("The first letter you entered was: " + THEY_SAID[:1])
