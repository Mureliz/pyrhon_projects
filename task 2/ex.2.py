n = int(input("Введите количество итераций:\n"))

'''
1)          2) *                3)     *
 *            * *                     * *
* *          *   *                   *   *
            * * * *                 * * * *
                                   *       *
                                  * *     * *
                                 *   *   *   *
                                * * * * * * * *
'''

triangle = [[0 for j in range(2**n)] for i in range(2**n)]
for i in range(len(triangle)):
    triangle[i][0] = 1
    triangle[i][i] = 1

for i in range(1, len(triangle)):
    for j in range(1, len(triangle[i])):
        triangle[i][j] = (triangle[i-1][j-1] + triangle[i-1][j]) % 2

count = 2 ** n
output = []
for i in range(len(triangle)):
    string = []
    string.append(count * ' ')
    for j in range(len(triangle[i])):
        if triangle[i][j] == 1:
            string.append('*')
        else:
            string.append(' ')
    count -= 1
    output.append(string)

max_len = len(output[-1])
for s in output:
    tmp_str = ''
    for n in s:
        tmp_str += n + ' '
    tmp_str = tmp_str.center(max_len)
    print(tmp_str)
