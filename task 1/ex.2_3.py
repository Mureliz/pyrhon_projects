n = int(input("Задайте число ступенек:\n"))
list_a = []

numbers = ''
for i in range(1, n+1):
    numbers += str(i)
    list_a.append(numbers[-1::-1] + numbers[1:])

max_len = len(list_a[n-1])
for i, s in enumerate(list_a):
    s = s.center(max_len)
    print(s)
    if i > 8:
        enter = '\n' * int((i+2)/100)
        print(enter)
