script = input()
for char in script:
    if char in ['H', 'Q', '9']:
        print("YES")
        exit()
print("NO")