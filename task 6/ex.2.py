fout = open("input2.txt", "r")
numbers = []
while True:
    string = fout.readline().rstrip('\n')
    if string == '':
        break
    numbers.append(int(string))
fout.close()

fin = open("output2.txt", "w")
numbers = sorted(numbers)
for n in numbers:
    print(str(n), file=fin)
fin.close()
