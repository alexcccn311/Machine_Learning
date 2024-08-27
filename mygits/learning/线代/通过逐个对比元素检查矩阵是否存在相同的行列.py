# 作者：Alex
# 2024/8/27 上午2:18
import numpy as np

A = np.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36],
    [37, 38, 39, 40, 41, 42]
])


def matrix_check(matrix):
    same_row, same_col, check_cols_result, check_rows_result = False, False, False, False
    rows, cols = matrix.shape
    for x in range(rows):
        for i in range(x+1,rows):
            if matrix[x, 0] == matrix[i, 0]:
                for j in range(cols):
                    if matrix[i, j] != matrix[x, j]:
                        break
                    elif j == cols-1:
                        check_rows_result = True
                        same_row = i
                        break
            if check_rows_result:
                break
        if check_rows_result:
            break
    for y in range(cols):
        for k in range(y+1, cols):
            if matrix[0, y] == matrix[0, k]:
                for s in range(rows):
                    if matrix[s, y] != matrix[s, k]:
                        break
                    elif s == rows -1:
                        check_cols_result = True
                        same_col = k
                        break
            if check_cols_result:
                break
        if check_cols_result:
            break
    # return check_rows_result, check_cols_result, same_row, same_col
    result = "检查结果: "
    if check_rows_result:
        result += f"有相同行（行号：{same_row + 1}）"
    else:
        result += "没有相同行"

    if check_cols_result:
        result += f"，有相同列（列号：{same_col + 1}）"
    else:
        result += "，没有相同列"

    print(result)

if __name__ == '__main__':
    matrix_check(A)
