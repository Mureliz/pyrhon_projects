n = int(input("Задайте число ступенек:\n"))

numbers = ''
indent = ' '*(n-1)
for i in range(1, n+1):
    numbers += str(i)
    print(indent + numbers + numbers[-2::-1])
    indent = indent[:-1]
