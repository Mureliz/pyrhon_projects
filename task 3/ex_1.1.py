string = input("Введите набор латинских букв:\n")
output = ''

for i, symbol in enumerate(string):
    if symbol in '23456789':
        output += string[i-1] * (int(symbol)-1)
    else:
        output += symbol

print(output)
