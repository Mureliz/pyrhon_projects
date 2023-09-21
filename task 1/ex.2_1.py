n = int(input("Задайте число ступенек:\n"))

# строками
string = ''
for i in range(1, n+1):
    string += str(i)
    print(string)

# числами
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, sep='', end='')
#     print()
