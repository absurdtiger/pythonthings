
file = open("txtfiletolist.txt", "r")

list = []
for line in file:
        stripped_line = line.strip()
        list.append(stripped_line)

file.close()

print(list)