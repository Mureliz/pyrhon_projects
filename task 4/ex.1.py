numbers = [19, 3, -5, 10, 0, -1, 32, 4, 18, 71, 16, 3, 9]
print(f"В списке {numbers}\nмаксимальный и минимальный элементы меняются местами:")
maxi = 0
mini = 0
for i in range(len(numbers)):
    if numbers[maxi] < numbers[i]:
        maxi = i
    if numbers[mini] > numbers[i]:
        mini = i
numbers[mini], numbers[maxi] = numbers[maxi], numbers[mini]
print(numbers)
