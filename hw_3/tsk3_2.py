import math
import typing

import numpy as np


class ConsoleDisplayMatrixMixin:
    def __str__(self) -> str:
        rows = []
        for row in self.data:
            rows.append(' '.join(map(str, row)))
        return '\n'.join(rows)


class ArithmeticMixin:
    def __add__(self, other: 'Matrix') -> 'Matrix':
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[i])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[i])):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(other.data[0])):
                element = 0
                for k in range(len(other.data)):
                    element += self.data[i][k] * other.data[k][j]
                row.append(element)
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

    def __truediv__(self, other: 'Matrix') -> 'Matrix':
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[i])):
                try:
                    row.append(self.data[i][j] / other.data[i][j])
                except (ZeroDivisionError, RuntimeWarning) as exc:
                    row.append(math.inf)
            result.append(row)
        return Matrix(result)


class FileMatrixOutputMixin:
    def save_to_file(self, filename: str) -> None:
        with open(filename, 'w') as file:
            for row in self.data:
                file.write(' '.join(map(str, row)) + '\n')


class Matrix(ArithmeticMixin, ConsoleDisplayMatrixMixin,
             FileMatrixOutputMixin):
    def __init__(self, data: typing.List[typing.List[int]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])


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

    print(matrix_left_cls_instance)  # check __str__
    print(" ")
    print(matrix_right_cls_instance)

    result_add = matrix_left_cls_instance + matrix_right_cls_instance
    result_add.save_to_file('matrix+.txt')

    result_sub = matrix_left_cls_instance - matrix_right_cls_instance
    result_sub.save_to_file('matrix-.txt')

    result_mul = matrix_left_cls_instance * matrix_right_cls_instance
    result_mul.save_to_file('matrix*.txt')

    result_matmul = matrix_left_cls_instance / matrix_right_cls_instance
    result_matmul.save_to_file('matrixDiv.txt')

    result_matmul = matrix_left_cls_instance @ matrix_right_cls_instance
    result_matmul.save_to_file('matrix@.txt')
