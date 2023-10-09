def sort(num, let):
    for i in range(len(num)):
        j = i - 1
        key = num[i]
        word = let[i]
        while num[j] < key and j >= 0:
            num[j + 1] = num[j]
            let[j + 1] = let[j]
            j -= 1
        num[j + 1] = key
        let[j + 1] = word


string = input("Введите набор латинских букв:\n")
string = string.replace(' ', '')
print('string без пробелов:', string, end='\n\n')

numbers = []
letters = []
count = 1

while string:
    symbol = string[0]
    string = string.replace(symbol, '', 1)

    for i in range(len(string)):
        if string[i] == symbol:
            count += 1
            string = string.replace(symbol, ' ', 1)

    numbers.append(count)
    letters.append(symbol)
    count = 1
    string = string.replace(' ', '')

sort(numbers, letters)
for i in range(3):
    print(numbers[i], letters[i], end='\n')
