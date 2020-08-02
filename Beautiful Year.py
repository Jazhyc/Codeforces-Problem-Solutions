year = int(input())

while True:

    year += 1
    nyear = str(year)
    digits = []

    for char in nyear:
        if char not in digits:
            digits.append(char)
        else:
            break
    
    if len(digits) == 4:
        print(nyear)
        exit()


