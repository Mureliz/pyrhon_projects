fout = open("input3.txt", "r", encoding="utf-8")
children = []
while True:
    string = fout.readline().rstrip('\n')
    if string == '':
        break
    child = [string[:-1], int(string[-1])]
    children.append(child)
fout.close()

children = sorted(children, key=lambda x: x[1])
youngest = children[0][0] + ' ' + str(children[0][1])
oldest = children[-1][0] + ' ' + str(children[-1][1])

fin = open("output3.1.txt", "w", encoding="utf-8")
fin.write(youngest)
fin.close()
fin = open("output3.2.txt", "w", encoding="utf-8")
fin.write(oldest)
fin.close()
