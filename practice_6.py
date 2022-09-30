# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    
    l = s.split()
    shortest = 0

    for word in l:
        if shortest == 0:
            shortest = len(word)
        elif len(word) < shortest:
            shortest = len(word)
    return shortest

print(find_short("Lets all go on holiday somewhere very cold"))