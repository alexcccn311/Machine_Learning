# 作者：Alex
# 2024/8/27 上午4:35
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
    same_row, same_col = -1, -1
    check_rows_result, check_cols_result = False, False
    rows, cols = matrix.shape

    # 检查是否有相同行
    for x in range(rows):
        for i in range(x + 1, rows):
            if np.array_equal(matrix[x], matrix[i]):
                check_rows_result = True
                same_row = i
                break
        if check_rows_result:
            break

    # 检查是否有相同列
    for y in range(cols):
        for k in range(y + 1, cols):
            if np.array_equal(matrix[:, y], matrix[:, k]):
                check_cols_result = True
                same_col = k
                break
        if check_cols_result:
            break

    # 打印结果
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
