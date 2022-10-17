# Complete the function scramble(str1, str2) that returns true if a portion of 
# str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.

# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

def scramble(s1, s2):
    # first attempt, set takes out duplicates
    # if (set(s2) & set(s1)) == set(s2):
    #     return True
    # return False

    # second attempt timed out, need more efficient solution
    # s1 = list(s1)
    # s2 = list(s2)
    # found = []
    # idx = 0
    
    # for element in s2:
    #     if element in s1:
    #         idx = s1.index(element)
    #         found.append(s1.pop(idx))

    # if found == s2:
    #     return True
    # return False

    # third attempt timed out, need more efficient solution
    for letter in s2:
        if s1.count(letter) >= s2.count(letter):
            continue
        else:
            return False
    return True

print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('hinybulodyjqxceiwpl', 'eqxjohyibuxpi'))
print(scramble('scriptingjava', 'javascript'))