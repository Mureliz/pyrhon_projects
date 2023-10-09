string = input("Введите набор латинских букв:\n")
output = ''
count = 1

for i, symbol in enumerate(string):
    if symbol == string[i-1]:
        count += 1
    else:
        if count > 1:
            output += str(count) + symbol
        else:
            output += symbol
        count = 1
if count > 1:
    output += str(count)

print(output)   # Y4g2ke3A3BV
