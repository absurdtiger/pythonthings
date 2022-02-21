# removes the first a from a string. this is just a test

def remove_a(word):
    i = word.find("a")
    print(i)
    word = word[:i] + word[i+1:]
    return word

print(remove_a("halp"))
