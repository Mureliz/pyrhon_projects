A_set = set(map(int, input("Введите элементы множества A: ").split()))
B_set = set(map(int, input("Введите элементы множества B: ").split()))

if A_set < B_set:
    print(True)
else:
    print(False)
