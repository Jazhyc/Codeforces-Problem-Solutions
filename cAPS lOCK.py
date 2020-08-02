text = input()
if (text[0].islower() and text[1 : len(text)].isupper()):
    text = text.capitalize()

elif text.isupper():
    text = text.lower()

elif text.islower() and len(text) == 1:
    text = text.upper()

print(text)