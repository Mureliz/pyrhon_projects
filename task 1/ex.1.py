a, b, c = map(int, input("Задайте три числа: ").split())
k = 0
if a == b and b == c:
    k = 3
elif a == b or a == c or c == b:
    k = 2
print("Одинаковых чисел", k)
