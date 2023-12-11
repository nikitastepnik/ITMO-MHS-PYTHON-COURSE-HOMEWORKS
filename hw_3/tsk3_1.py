import typing

import numpy as np


class Matrix:
    def __init__(self, data: typing.List[typing.List[int]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                "Invalid matrix dimensions: "
                f"A({self.rows}; {self.cols}); "
                f"B({other.rows}; {other.cols})"
            )
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                "Invalid matrix dimensions: "
                f"A({self.rows}; {self.cols}); "
                f"B({other.rows}; {other.cols})"
            )
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] * other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        if self.cols != other.rows:
            raise ValueError(
                "Invalid matrix dimensions for matrix multing: "
                f"A({self.rows}; {self.cols}); "
                f"B({other.rows}; {other.cols})"
            )
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                element = 0
                for k in range(self.cols):
                    element += self.data[i][k] * other.data[k][j]
                row.append(element)
            result.append(row)
        return Matrix(result)


if __name__ == '__main__':
    np.random.seed(0)

    matrix_raw_left = list(map(list, np.random.randint(0, 10, (10, 10))))
    matrix_raw_right = list(map(list, np.random.randint(0, 10, (10, 10))))

    with open('matrix_left.txt', 'w') as file:
        for row in matrix_raw_left:
            file.write(' '.join(map(str, row)) + '\n')

    with open('matrix_right.txt', 'w') as file:
        for row in matrix_raw_right:
            file.write(' '.join(map(str, row)) + '\n')

    matrix_left_cls_instance = Matrix(matrix_raw_left)
    matrix_right_cls_instance = Matrix(matrix_raw_right)

    result_add = matrix_left_cls_instance + matrix_right_cls_instance
    with open('matrix+.txt', 'w') as file:
        for row in result_add.data:
            file.write(' '.join(map(str, row)) + '\n')

    result_mul = matrix_left_cls_instance * matrix_right_cls_instance
    with open('matrix*.txt', 'w') as file:
        for row in result_mul.data:
            file.write(' '.join(map(str, row)) + '\n')

    result_matmul = matrix_left_cls_instance @ matrix_right_cls_instance
    with open('matrix@.txt', 'w') as file:
        for row in result_matmul.data:
            file.write(' '.join(map(str, row)) + '\n')
