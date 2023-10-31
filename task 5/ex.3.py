n = int(input("Сколько городов уже было названо? "))
cities = set()
print("Перечислите их.")
for _ in range(n):
    cities.add(input())

city = input("Следующий город:\n")
while city != '0':
    if city in cities:
        print("REPEAT")
        city = input()
    else:
        print("OK")
        cities.add(city)
        city = input("Следующий город:\n")
