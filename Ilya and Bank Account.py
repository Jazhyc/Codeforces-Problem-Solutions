bank = input()
balance = list(bank)

if int(bank) < -10:
    if balance[-2] > balance[-1]:
        balance.pop(-2)
    else:
        balance.pop(-1)

print(int(''.join(balance)))
