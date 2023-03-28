order = int(input())
matrix = []
for i in range(order):
    row = input().split()
    matrix.append(row)

def diagonalDifference(matrix):
    lr_sum = 0
    rl_sum = 0
    for i in range(len(matrix)):
        lr_sum = lr_sum + int(matrix[i][i])
        rl_sum = rl_sum + int(matrix[i][(len(matrix)-1)-i])
    return abs(lr_sum - rl_sum)

print(diagonalDifference(matrix))


