def persistence(n):
    nn = list(str(n))
    result = 1
    for x in nn:
        result = result * int(x)
    if len(str(result)) != 1:
        for x in str(result):
            new_res = 1
            new_res = new_res * int(x)
    return new_res
    # while len(n) != 1:
    #     i = 0
    #     if i != len(n) - 1:
    #         nn = int(n[i])
            


print(persistence(999))