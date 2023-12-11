import numpy as np


class MatrixMixin:
    def __init__(self, data):
        self._data = np.array(data)

    @property
    def data(self):
        return self._data.tolist()

    @data.setter
    def data(self, new_data):
        self._data = np.array(new_data)

    def __str__(self):
        return str(self._data)


class ArithmeticMixin:
    def __add__(self, other):
        result = self._data + other._data
        return Matrix(result)

    def __sub__(self, other):
        result = self._data - other._data
        return Matrix(result)

    def __mul__(self, other):
        result = self._data * other._data
        return Matrix(result)

    def __div__(self, other):
        result = self._data / other._data
        return Matrix(result)


class FileIOMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self._data:
                file.write(' '.join(map(str, row)) + '\n')


class Matrix(MatrixMixin, ArithmeticMixin, FileIOMixin):
    pass
