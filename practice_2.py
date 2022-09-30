# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    
    pos_list = [num for num in arr if num >= 0]
    
    if len(pos_list) == 0:
        return 0
    else:
        return sum(pos_list)

print(positive_sum([-1,-2,-3,-4,-5]))