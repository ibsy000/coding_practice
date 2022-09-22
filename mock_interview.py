# Given a word w and some text t, find whether w is in t. 
# For example: w="nest", t="I built a nest and tested it."

def find_whether(word, text):

    text_list = text.split()
    if word in text_list:
        return True
    return False

print(find_whether('nest', 'I built a nest and tested it'))

# linear time and linear space => O(n)
# sliding window would be more efficient