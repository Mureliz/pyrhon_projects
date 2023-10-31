fout = open("input1.txt", "r")
numbers = list(map(int, fout.readline().split()))
fout.close()

product = 1
for n in numbers:
    product *= n

fin = open("output1.txt", "w")
fin.write(str(product))
