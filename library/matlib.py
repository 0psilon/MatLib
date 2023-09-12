from check import MatrixCheck, MatrixException


class Matrix:
    def __init__(self, matrix: list[list[float | int]]):
        
        self.matrix = MatrixCheck(matrix=matrix).matrix

    @property
    def T(self):
        return self._transpose()

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
        obj = '\n'.join([' ' + str(line).rjust(1) for line in self.matrix])
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
            raise ArithmeticError('Operand is supposed to be int, float or an instance of the Matrix class')
        
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
            raise ArithmeticError('Operand is supposed to be int, float or an instance of the Matrix class')
        
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
            raise ArithmeticError('Operand is supposed to be int, float or an instance of the Matrix class')
        
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
            raise ArithmeticError('Operand is supposed to be int, float or an instance of the Matrix class')
        
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
