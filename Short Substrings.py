n = int(input())

for i in range(n):

    string = input()

    if len(string) <= 2:
        print(string)
    
    else:
        for j in range(0, len(string), 2):
            print(string[j], end='')
        print(string[-1], end='')
        print()