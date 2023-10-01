n = int(input("Задайте число уровней:\n"))
triangle = []

for i in range(0, n):
    numbers = []
    for j in range(0, i+1):
        if j == 0 or j == i:
            numbers.append(1)
        else:
            if j <= int(i/2):
                numbers.append(triangle[i-1][j-1] + triangle[i-1][j])
            elif i % 2 == 0:
                numbers.extend(numbers[-2::-1])
                break
            else:
                numbers.extend(numbers[::-1])
                break
    triangle.append(numbers)

last_el = triangle[-1]
new_le = ''
for n in last_el:
    n = str(n)
    new_le += n + ' '
max_len = len(new_le)-1

for s in triangle:
    tmp_str = ''
    for n in s:
        n = str(n)
        tmp_str += n + ' '
    tmp_str = tmp_str.center(max_len)
    print(tmp_str)
