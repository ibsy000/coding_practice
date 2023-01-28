# This time no story, no theory. The examples below show you how to write 
# function accum:

### Examples:
### accum("abcd") -> "A-Bb-Ccc-Dddd"
### accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
### accum("cwAt") -> "C-Ww-Aaa-Tttt"

# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(s):
    # create a new string to append each character from the original string
    new_string = ''
    position = 1

    for char in s:
        # append the first character in upper and the remaining characters in lower
        # multiplied by the position's index 
        new_string += char.upper() + (char.lower() * (position - 1))
        # if the position is not the last character add a hyphen to the new string
        if position != len(s):
            new_string += '-'
        # increase the position by one for each character
        position += 1
    return new_string

print(accum("abcd"))