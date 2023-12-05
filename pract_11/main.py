import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
import csv

# 1_________________________________________________________________
# Установка частоты и амплитуды для прямоугольных волн
frequency = 5
amplitude = 1

# Генерация значений от 0 до 1 с шагом 0.001
axisX = np.arange(0, 1, 0.001)

# Генерация прямоугольных волн сигнала используя частоту и амлпитуду
period = 1.0 / frequency
axisY = amplitude * square(2 * np.pi * frequency * axisX)

# Визуализация результата
plt.plot(axisX, axisY)
plt.grid(True)
plt.show()


# 2_________________________________________________________________
# Генерация случайных чисел из нормального распределения
n = 1000
mean = 0  # мат. ожидание
stddev = 1  # стандартное отклонение
X = np.random.normal(mean, stddev, size=(n,))

# Отрисовка гистограммы
plt.hist(X, bins=80)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()


# 3_________________________________________________________________
# Загрузка данных из CSV файла
data = []
with open('passengers.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Пропуск заголовка
    for row in reader:
        data.append(int(row[1]))  # Второй столбец содержит количество пассажиров

# График пассажиропотока за все время (линейный график)
plt.plot(data)
plt.xlabel('Месяц')
plt.ylabel('Количество пассажиров')
plt.title('Пассажиропоток за все время')
plt.grid(True)
plt.show()

# Распределение пассажиров по месяцам в 1951-1955 гг. (гистограмма)
years = range(1951, 1956)
monthly_data = [data[i:i+12] for i in range(0, len(data), 12)]  # Разделение данных по годам
for i, year in enumerate(years):
    plt.hist(monthly_data[i], bins=12, alpha=0.7, label=str(year))
plt.xlabel('Месяц')
plt.ylabel('Количество пассажиров')
plt.title('Распределение пассажиров по месяцам (1951-1955)')
plt.legend()
plt.grid(True)
plt.show()
