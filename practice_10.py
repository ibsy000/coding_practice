# https://www.codewars.com/kata/514a024011ea4fb54200004b
# Write a function that when given a URL as a string, parses out just the domain 
# name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    first_idx = 0
    second_idx = 0

    for num in range(len(url)):
        print(num, url[num])
        if url[num] == '/' and first_idx == 0:
            first_idx = num + 1
        if url[num] == '.':
            second_idx = num
        if url[num] == '.' and num != second_idx:
            first_idx = num
    print(first_idx, second_idx)
    print(url[first_idx + 1:second_idx])

print(domain_name("http://www.zombie-bites.com"))