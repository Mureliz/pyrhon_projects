import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import matplotlib.animation as animation
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# 1. Построение графиков полиномов Лежандра
x = np.linspace(-1, 1, 400)
plt.figure()

for n in range(1, 8):
    y = sp.eval_legendre(n, x)
    plt.plot(x, y, label=f'n = {n}')

plt.title('Полиномы Лежандра')
plt.legend()
plt.show()


# 2. Отрисовка ряда из фигур Лисажу
t = np.linspace(0, 2*np.pi, 1000)

frequencies = [(3, 2), (3, 4), (5, 4), (5, 6)]

plt.figure(figsize=(12, 12))

for i, (f1, f2) in enumerate(frequencies):
    x = np.sin(f1 * t)
    y = np.sin(f2 * t)

    plt.subplot(2, 2, i + 1)
    plt.plot(x, y)
    plt.title(f'Соотношение частот: {f1}:{f2}')
    plt.xlabel('sin(' + str(f1) + 't)')
    plt.ylabel('sin(' + str(f2) + 't)')

plt.show()

# 3. Анимация вращения фигуры Лисажу
fig, ax = plt.subplots()

t = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(np.sin(t), np.sin(t))


def animate(i):
    line.set_xdata(np.sin((i+1) * t))
    line.set_ydata(np.sin((i+2) * t))
    return line,


ani = animation.FuncAnimation(
    fig, animate, frames=100, interval=50)

plt.show()

# 4. Моделирование сложения двух волн с интерактивным слайдером

# Генерация синусных волн
t = np.linspace(0, 2*np.pi, 1000)
frequency_1, amplitude_1 = 1.0, 1.0
frequency_2, amplitude_2 = 1.5, 1.0

fig, ax = plt.subplots()
line, = ax.plot(t, amplitude_1 * np.sin(frequency_1 * t) + amplitude_2 * np.sin(frequency_2 * t),
                linewidth=2, color='r')

ax_frequency1 = plt.axes([0.15, 0.02, 0.3, 0.02])
ax_amplitude1 = plt.axes([0.15, 0.06, 0.3, 0.02])
ax_frequency2 = plt.axes([0.55, 0.02, 0.3, 0.02])
ax_amplitude2 = plt.axes([0.55, 0.06, 0.3, 0.02])

slider_frequency1 = Slider(ax_frequency1, 'Частота 1', 0.1, 2.0, valinit=frequency_1)
slider_amplitude1 = Slider(ax_amplitude1, 'Амплитуда 1', 0.1, 2.0, valinit=amplitude_1)
slider_frequency2 = Slider(ax_frequency2, 'Частота 2', 0.1, 2.0, valinit=frequency_2)
slider_amplitude2 = Slider(ax_amplitude2, 'Амплитуда 2', 0.1, 2.0, valinit=amplitude_2)


def update(val):
    frequency_1 = slider_frequency1.val
    amplitude_1 = slider_amplitude1.val
    frequency_2 = slider_frequency2.val
    amplitude_2 = slider_amplitude2.val
    line.set_ydata(amplitude_1 * np.sin(frequency_1 * t) + amplitude_2 * np.sin(frequency_2 * t))
    fig.canvas.draw_idle()


slider_frequency1.on_changed(update)
slider_amplitude1.on_changed(update)
slider_frequency2.on_changed(update)
slider_amplitude2.on_changed(update)

plt.show()

# 5. Отрисовка графиков среднеквадратчиного отклонения MS
# и реазия оси z на втором в логарифмическом масштабе.

# Генерация случайных данных
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# Вычисление среднеквадратичного отклонения MSE
mse = (x - y) ** 2

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

ax1.scatter(x, y, z, c='r', marker='o')
ax1.set_title('MSE')

ax2.scatter(x, y, mse, c='g', marker='^')
ax2.set_yscale('log')
ax2.set_title('MSE в логарифмическом масштабе (z-ось)')

plt.show()
