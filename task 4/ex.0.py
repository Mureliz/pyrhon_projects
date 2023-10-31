numbers = [19, 3, 10, 0, -1, 32, 4, 18, 71, 16, 3, 9]

output = []
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        output.append(numbers[i])
print(f"В списке {numbers}\nэлементы, которые больше предыдущего:\n{output}")
