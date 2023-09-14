import os

from .check import MatrixCheck, MatrixException


class Matrix:
    def __init__(self, matrix: list[list[float | int]]):
        
        self.matrix = MatrixCheck(matrix=matrix).matrix
        self.n_digits = os.environ.get('n_digits')

        if self.n_digits.isdigit():
            self.n_digits = int(self.n_digits)
        
        else:
            self.n_digits = 3

    @property
    def T(self):
        return self._transpose()
    
    @property
    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def _transpose(self):
        n, m = len(self.matrix), len(self.matrix[0])
        matrix_T = [[0.] * n for _ in range(m)]
            
        for i in range(m):
            for j in range(n):
                matrix_T[i][j] = self.matrix[j][i]

        return Matrix(matrix_T)

    def __len__(self):
        return len(self.matrix)
    
    def __str__(self):        
        flag = False
        n, m = len(self.matrix), len(self.matrix[0])
        check = [el for line in self.matrix for el in line]
        mx = max([len(str(x).split('.')[0]) for x in check])

        if min(check) < 0:
            flag = True

        new_matrix = [[None] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                new_matrix[i][j] = f'{self.matrix[i][j]:.{self.n_digits}f}'\
                    .rjust((self.n_digits + mx + 1) if flag else (self.n_digits + mx))
            new_matrix[i] = '[' + ' '.join(new_matrix[i]) + ']'

        obj = '\n'.join([' ' + str(line).rjust(1) for line in new_matrix])
        obj = '[' + obj[1:] + ']'

        return obj
        
    def __getitem__(self, item):
        if isinstance(item, int):
            return self.matrix[item]

        else:
            raise TypeError('Index must be an integer')
    
    def __add__(self, ent):        
        res_matrix = [[None] * len(self.matrix[0]) \
                      for _ in range(len(self.matrix))]

        if isinstance(ent, (int, float)):            
            for i, line in enumerate(self.matrix):
                for j, el in enumerate(line):
                    res_matrix[i][j] = el + ent
            
            return Matrix(res_matrix)

        elif isinstance(ent, Matrix):
            if len(self.matrix) != len(ent):
                raise MatrixException('Matrices have incompatible lengths')

            for i, line in enumerate(self.matrix):                
                if len(line) != len(ent[i]):
                    raise MatrixException('Matrices have arbitrary dimensions')

                for j, el in enumerate(line):
                    res_matrix[i][j] = el + ent.matrix[i][j]
        
            return Matrix(res_matrix)
        
        else:
            raise ArithmeticError('Right operand is supposed to be int, float or an instance of the Matrix class')
    
    def __radd__(self, ent):
        if isinstance(ent, (int, float)):
            return self + ent
        
        else:
            raise ArithmeticError('Left operand is supposed to be int or float')
    
    def __iadd__(self, ent):
        if isinstance(ent, (int, float)):            
            for i, line in enumerate(self.matrix):
                for j, _ in enumerate(line):
                    self.matrix[i][j] += ent
            
            return self

        elif isinstance(ent, Matrix):
            if len(self.matrix) != len(ent):
                raise MatrixException('Matrices have incompatible lengths')

            for i, line in enumerate(self.matrix):                
                if len(line) != len(ent[i]):
                    raise MatrixException('Matrices have arbitrary dimensions')

                for j, _ in enumerate(line):
                    self.matrix[i][j] += ent.matrix[i][j]
        
            return self
        
        else:
            raise ArithmeticError('Right operand is supposed to be int, float or an instance of the Matrix class')
        
    def __sub__(self, ent):        
        res_matrix = [[None] * len(self.matrix[0]) \
                      for _ in range(len(self.matrix))]

        if isinstance(ent, (int, float)):          
            for i, line in enumerate(self.matrix):
                for j, el in enumerate(line):
                    res_matrix[i][j] = el - ent
            
            return Matrix(res_matrix)

        elif isinstance(ent, Matrix):
            if len(self.matrix) != len(ent):
                raise MatrixException('Matrices have incompatible lengths')

            for i, line in enumerate(self.matrix):                
                if len(line) != len(ent[i]):
                    raise MatrixException('Matrices have arbitrary dimensions')

                for j, el in enumerate(line):
                    res_matrix[i][j] = el - ent.matrix[i][j]
        
            return Matrix(res_matrix)
        
        else:
            raise ArithmeticError('Right operand is supposed to be int, float or an instance of the Matrix class')
        
    def __rsub__(self, ent):
        if isinstance(ent, (int, float)):
            return self - ent
        
        else:
            raise ArithmeticError('Left operand is supposed to be int or float')

    def __isub__(self, ent):
        if isinstance(ent, (int, float)):            
            for i, line in enumerate(self.matrix):
                for j, _ in enumerate(line):
                    self.matrix[i][j] -= ent
            
            return self

        elif isinstance(ent, Matrix):
            if len(self.matrix) != len(ent):
                raise MatrixException('Matrices have incompatible lengths')

            for i, line in enumerate(self.matrix):                
                if len(line) != len(ent[i]):
                    raise MatrixException('Matrices have arbitrary dimensions')

                for j, _ in enumerate(line):
                    self.matrix[i][j] -= ent.matrix[i][j]
        
            return self
        
        else:
            raise ArithmeticError('Right operand is supposed to be int, float or an instance of the Matrix class')
        
    def __mul__(self, ent):        
        res_matrix = [[None] * len(self.matrix[0]) \
                      for _ in range(len(self.matrix))]

        if isinstance(ent, (int, float)):            
            for i, line in enumerate(self.matrix):
                for j, el in enumerate(line):
                    res_matrix[i][j] = el * ent
            
            return Matrix(res_matrix)

        elif isinstance(ent, Matrix):
            if len(self.matrix) != len(ent):
                raise MatrixException('Matrices have incompatible lengths')

            for i, line in enumerate(self.matrix):                
                if len(line) != len(ent[i]):
                    raise MatrixException('Matrices have arbitrary dimensions')

                for j, el in enumerate(line):
                    res_matrix[i][j] = el * ent.matrix[i][j]
        
            return Matrix(res_matrix)
        
        else:
            raise ArithmeticError('Right operand is supposed to be int, float or an instance of the Matrix class')

    def __rmul__(self, ent):
        if isinstance(ent, (int, float)):
            return self * ent
        
        else:
            raise ArithmeticError('Left operand is supposed to be int or float')

    def __imul__(self, ent):
        if isinstance(ent, (int, float)):            
            for i, line in enumerate(self.matrix):
                for j, _ in enumerate(line):
                    self.matrix[i][j] *= ent
            
            return self

        elif isinstance(ent, Matrix):
            if len(self.matrix) != len(ent):
                raise MatrixException('Matrices have incompatible lengths')

            for i, line in enumerate(self.matrix):                
                if len(line) != len(ent[i]):
                    raise MatrixException('Matrices have arbitrary dimensions')

                for j, _ in enumerate(line):
                    self.matrix[i][j] *= ent.matrix[i][j]
        
            return self
        
        else:
            raise ArithmeticError('Right operand is supposed to be int, float or an instance of the Matrix class')
        
    def __truediv__(self, ent):        
        res_matrix = [[None] * len(self.matrix[0]) \
                      for _ in range(len(self.matrix))]

        if isinstance(ent, (int, float)):            
            for i, line in enumerate(self.matrix):
                for j, el in enumerate(line):
                    res_matrix[i][j] = el / ent
            
            return Matrix(res_matrix)

        elif isinstance(ent, Matrix):
            if len(self.matrix) != len(ent):
                raise MatrixException('Matrices have incompatible lengths')

            for i, line in enumerate(self.matrix):                
                if len(line) != len(ent[i]):
                    raise MatrixException('Matrices have arbitrary dimensions')

                for j, el in enumerate(line):
                    res_matrix[i][j] = el / ent.matrix[i][j]
        
            return Matrix(res_matrix)
        
        else:
            raise ArithmeticError('Right operand is supposed to be int, float or an instance of the Matrix class')
    
    def __rtruediv__(self, ent):
        if isinstance(ent, (int, float)):
            return self / ent
        
        else:
            raise ArithmeticError('Left operand is supposed to be int or float')
    
    def __itruediv__(self, ent):
        if isinstance(ent, (int, float)):            
            for i, line in enumerate(self.matrix):
                for j, _ in enumerate(line):
                    self.matrix[i][j] /= ent
            
            return self

        elif isinstance(ent, Matrix):
            if len(self.matrix) != len(ent):
                raise MatrixException('Matrices have incompatible lengths')

            for i, line in enumerate(self.matrix):                
                if len(line) != len(ent[i]):
                    raise MatrixException('Matrices have arbitrary dimensions')

                for j, _ in enumerate(line):
                    self.matrix[i][j] /= ent.matrix[i][j]
        
            return self
        
        else:
            raise ArithmeticError('Right operand is supposed to be int, float or an instance of the Matrix class')
    
    def __floordiv__(self, ent):        
        res_matrix = [[None] * len(self.matrix[0]) \
                      for _ in range(len(self.matrix))]

        if isinstance(ent, (int, float)):            
            for i, line in enumerate(self.matrix):
                for j, el in enumerate(line):
                    res_matrix[i][j] = el // ent
            
            return Matrix(res_matrix)

        elif isinstance(ent, Matrix):
            if len(self.matrix) != len(ent):
                raise MatrixException('Matrices have incompatible lengths')

            for i, line in enumerate(self.matrix):                
                if len(line) != len(ent[i]):
                    raise MatrixException('Matrices have arbitrary dimensions')

                for j, el in enumerate(line):
                    res_matrix[i][j] = el // ent.matrix[i][j]
        
            return Matrix(res_matrix)
        
        else:
            raise ArithmeticError('Right operand is supposed to be int, float or an instance of the Matrix class')
    
    def __rfloordiv__(self, ent):
        if isinstance(ent, (int, float)):
            return self // ent
        
        else:
            raise ArithmeticError('Left operand is supposed to be int or float')
    
    def __ifloordiv__(self, ent):
        if isinstance(ent, (int, float)):            
            for i, line in enumerate(self.matrix):
                for j, _ in enumerate(line):
                    self.matrix[i][j] //= ent
            
            return self

        elif isinstance(ent, Matrix):
            if len(self.matrix) != len(ent):
                raise MatrixException('Matrices have incompatible lengths')

            for i, line in enumerate(self.matrix):                
                if len(line) != len(ent[i]):
                    raise MatrixException('Matrices have arbitrary dimensions')

                for j, _ in enumerate(line):
                    self.matrix[i][j] //= ent.matrix[i][j]
        
            return self
        
        else:
            raise ArithmeticError('Right operand is supposed to be int, float or an instance of the Matrix class')
    
    def __mod__(self, ent):        
        res_matrix = [[None] * len(self.matrix[0]) \
                      for _ in range(len(self.matrix))]

        if isinstance(ent, (int, float)):            
            for i, line in enumerate(self.matrix):
                for j, el in enumerate(line):
                    res_matrix[i][j] = el % ent
            
            return Matrix(res_matrix)

        elif isinstance(ent, Matrix):
            if len(self.matrix) != len(ent):
                raise MatrixException('Matrices have incompatible lengths')

            for i, line in enumerate(self.matrix):                
                if len(line) != len(ent[i]):
                    raise MatrixException('Matrices have arbitrary dimensions')

                for j, el in enumerate(line):
                    res_matrix[i][j] = el % ent.matrix[i][j]
        
            return Matrix(res_matrix)
        
        else:
            raise ArithmeticError('Right operand is supposed to be int, float or an instance of the Matrix class')
    
    def __rmod__(self, ent):
        if isinstance(ent, (int, float)):
            return self % ent
        
        else:
            raise ArithmeticError('Left operand is supposed to be int or float')
    
    def __imod__(self, ent):
        if isinstance(ent, (int, float)):            
            for i, line in enumerate(self.matrix):
                for j, _ in enumerate(line):
                    self.matrix[i][j] %= ent
            
            return self

        elif isinstance(ent, Matrix):
            if len(self.matrix) != len(ent):
                raise MatrixException('Matrices have incompatible lengths')

            for i, line in enumerate(self.matrix):                
                if len(line) != len(ent[i]):
                    raise MatrixException('Matrices have arbitrary dimensions')

                for j, _ in enumerate(line):
                    self.matrix[i][j] %= ent.matrix[i][j]
        
            return self
        
        else:
            raise ArithmeticError('Right operand is supposed to be int, float or an instance of the Matrix class')
        
    def __matmul__(self, ent):        
        if isinstance(ent, Matrix):

            n, m = len(self.matrix), len(self.matrix[0])
            d, k = len(ent.matrix), len(ent.matrix[0])

            if d != m:
                raise MatrixException('Matrix dimensions are incompatible')

            for line_1, line_2 in zip(self.matrix, ent):
                if len(line_1) != m:
                    raise MatrixException('Matrix 1 has arbitrary dimensions')
            
                if len(line_2) != k:
                    raise MatrixException('Matrix 2 has arbitrary dimensions')       
            
            res_matrix = [[0.] * k for _ in range(n)]

            # resulting matrix calculation
            for i in range(n): 
                for v in range(k):
                    for j in range(m):
                        res_matrix[i][v] += self.matrix[i][j] * ent.matrix[j][v]
            
            return Matrix(res_matrix)             
         
        else:
            raise ArithmeticError('Operand is supposed to be an instance of the Matrix class')
        
    def __pow__(self, exp):    
        if not isinstance(exp, int):
            raise TypeError('Exponent must be of the type integer')

        if exp <= 0:
            raise TypeError('Exponent must be positive')
        
        exp -= 1
        n = len(self.matrix)
        
        for line in self.matrix:
            if len(line) != n:
                raise MatrixException('Given matrix is not a square matrix')
        
        base = self.matrix.copy()

        while exp > 0:
            result = [[0.] * n for _ in range(n)]

            for i in range(n):
                for v in range(n):
                    for j in range(n):
                        result[i][v] += base[i][j] * self.matrix[j][v]

            base = result.copy()        
            exp -= 1
        
        return Matrix(base)
