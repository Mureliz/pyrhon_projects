import numpy as np
import numpy.random as rand
from scipy.linalg import cholesky
import scipy.stats


# 1 _______________________________________________________
# Прочитать матрицу из файла. Найти для этой матрицы
# сумму всех элементов, максимальный и минимальный элемент

print('1.', '_' * 85)
matrix = np.loadtxt("task1.txt", dtype='int', delimiter=',')
print('\n', matrix)

summa = matrix.sum()
max_e = matrix.max()
min_e = matrix.min()
print(summa, max_e, min_e)

# 2 ________________________________________________________
# Реализовать кодирование длин серий (Run-length encoding).
# Дан вектор x. Необходимо вернуть кортеж из двух векторов
# одинаковой длины. Первый содержит числа,
# а второй - сколько раз их нужно повторить.
print('\n2.', '_' * 85)

# x = list(map(int, input("Введите вектор: ").split()))
x = [2, 2, 2, 3, 3, 3, 5]
vector = np.array(x)
result = np.unique(vector, return_counts=True)

print('Результат кодирования:', result)

# 3 ________________________________________________________
# Написать программу NumPy генерирующую массив случайных
# чисел нормального распределения размера 10х4. Найти
# минимальное, максимальное, средние значения, стандартное
# отклонение. Сохранить первые 5 строк в отдельную переменную.
print('\n3.', '_' * 85)

array = rand.normal(size=(10, 4))

min_e = array.min()
max_e = array.max()
mean_v = array.mean()  # среднее значение
stddev = array.std()  # стандартное отклонение

first_five = array[:5]

print(f'Минимальное значение: {min_e},\n'
      f'Максимальное значение: {max_e},\n'
      f'Среднее значение: {mean_v},\n'
      f'Стандартное отклонение: {stddev}.\n'
      f'\nПервые пять строк:\n{first_five}.\n')

# 4 ________________________________________________________
# Найти максимальный элемент в векторе x среди элементов,
# перед которыми стоит нулевой
print('\n4.', '_' * 85)

# x = list(map(int, input("Введите вектор: ").split()))
x = [6, 2, 0, 3, 0, 0, 5, 7, 0]
vector = np.array(x)
idx = np.where(vector[:-1] == 0)[0]
max_e = np.max(vector[idx + 1])
print("Вектор:", vector)
print("Максимальный элемент среди элементов, перед которыми стоит нулевой:", max_e)


# 5 ________________________________________________________
# Реализовать функцию вычисления логарифма плотности
# многомерного нормального распределения.
# Входные параметры: точки X, размер (N, D), мат. ожидание m,
# вектор длины D, матрица ковариаций C, размер (D, D).
# Разрешается использовать библиотечные функции для подсчета
# определителя матрицы, а также обратной матрицы, в том числе
# в невекторизованном варианте. Сравнить с
# scipy.stats.multivariate_normal(m, C).logpdf(X)
# как по скорости работы, так и по точности вычислений.
print('\n5.', '_' * 85)


def log_multivariate_normal(X, m, C):
    D = m.shape[0]
    diff = X - m
    log_det = np.log(np.linalg.det(C))
    chol_C = cholesky(C, lower=True)
    quad_form = np.sum((np.linalg.solve(chol_C, diff.T).T) ** 2, axis=1)
    log_prob = -0.5 * (D * np.log(2 * np.pi) + log_det + quad_form)
    return log_prob


# тестовые данные
np.random.seed(0)
X = np.random.rand(1000, 2)
m = np.array([0.5, 0.5])
C = np.array([[2, 1], [1, 2]])

# вычисление логарифма плотности многомерного нормального распределения
custom_results = log_multivariate_normal(X, m, C)
# использование встроенной функции scipy
scipy_results = scipy.stats.multivariate_normal(m, C).logpdf(X)

# сравнение результатов - выдаёт True, значит они одинаковы по скорости и точности вычислений
print(np.allclose(custom_results, scipy_results))


# 6 ______________________________________________________________________
# Поменять местами две строки в двумерном массиве NumPy - поменяйте строки
# 1 и 3 массива а.  a = np.arange(16).reshape(4,4)
print('\n6.', '_' * 85)

a = np.arange(16).reshape(4, 4)
print("Массив a")
print(a)

print("Поменяли 1 и 3 строчку")
a[[0, 2]] = a[[2, 0]]
print(a)


# 7 ________________________________________________________
# Найти уникальные значения и их количество в столбце species таблицы iris
print('\n7.', '_' * 85)

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species = iris[:,-1]
result = np.unique(species, return_counts=True)
print(result)

# 8 ________________________________________________________
# Найти индексы ненулевых элементов
print('\n8.', '_' * 85)

vector = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
idx = np.where(vector == 0)[0]
print(*idx, sep=', ')
