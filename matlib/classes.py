from typing import Union

from .type_check import MatrixCheck


class Matrix:

    def __init__(self,
                 matrix: list[list[float | int]]):
        
        self.matrix = MatrixCheck(matrix=matrix).matrix

    def __len__(self):
        return len(self.matrix)
    
    def __add__(self, ent):
        
        res_matrix = [[None] * len(self.matrix[0]) \
                      for _ in range(len(self.matrix))]

        if isinstance(ent, (int, float)):
            
            for i, line in enumerate(self.matrix):
                for j, el in enumerate(line):
                    res_matrix[i][j] = el + ent
            
            return Matrix(res_matrix)

        elif isinstance(ent, Matrix):

            assert len(self.matrix) == len(ent.matrix), \
                'Matrices have incompatible lengths'

            for i, line in enumerate(self.matrix):
                
                assert len(line) == len(ent.matrix[i]), \
                    'Matrices have arbitrary dimensions'

                for j, el in enumerate(line):
                    res_matrix[i][j] = el + ent.matrix[i][j]
        
            return Matrix(res_matrix)
        
        else:
            raise ArithmeticError('Operand is supposed to be int, \
                                  float or an instance of the Matrix class')
        
    def __sub__(self, ent):
        
        res_matrix = [[None] * len(self.matrix[0]) \
                      for _ in range(len(self.matrix))]

        if isinstance(ent, (int, float)):
            
            for i, line in enumerate(self.matrix):
                for j, el in enumerate(line):
                    res_matrix[i][j] = el - ent
            
            return Matrix(res_matrix)

        elif isinstance(ent, Matrix):

            assert len(self.matrix) == len(ent.matrix), \
                'Matrices have incompatible lengths'

            for i, line in enumerate(self.matrix):
                
                assert len(line) == len(ent.matrix[i]), \
                    'Matrices have arbitrary dimensions'

                for j, el in enumerate(line):
                    res_matrix[i][j] = el - ent.matrix[i][j]
        
            return Matrix(res_matrix)
        
        else:
            raise ArithmeticError('Operand is supposed to be int, \
                                  float or an instance of the Matrix class')
        
    def __mul__(self, ent):
        
        res_matrix = [[None] * len(self.matrix[0]) \
                      for _ in range(len(self.matrix))]

        if isinstance(ent, (int, float)):
            
            for i, line in enumerate(self.matrix):
                for j, el in enumerate(line):
                    res_matrix[i][j] = el * ent
            
            return Matrix(res_matrix)

        elif isinstance(ent, Matrix):

            assert len(self.matrix) == len(ent.matrix), \
                'Matrices have incompatible lengths'

            for i, line in enumerate(self.matrix):
                
                assert len(line) == len(ent.matrix[i]), \
                    'Matrices have arbitrary dimensions'

                for j, el in enumerate(line):
                    res_matrix[i][j] = el * ent.matrix[i][j]
        
            return Matrix(res_matrix)
        
        else:
            raise ArithmeticError('Operand is supposed to be int, \
                                  float or an instance of the Matrix class')
        
    def __truediv__(self, ent):
        
        res_matrix = [[None] * len(self.matrix[0]) \
                      for _ in range(len(self.matrix))]

        if isinstance(ent, (int, float)):
            
            for i, line in enumerate(self.matrix):
                for j, el in enumerate(line):
                    res_matrix[i][j] = el / ent
            
            return Matrix(res_matrix)

        elif isinstance(ent, Matrix):

            assert len(self.matrix) == len(ent.matrix), \
                'Matrices have incompatible lengths'

            for i, line in enumerate(self.matrix):
                
                assert len(line) == len(ent.matrix[i]), \
                    'Matrices have arbitrary dimensions'

                for j, el in enumerate(line):
                    res_matrix[i][j] = el / ent.matrix[i][j]
        
            return Matrix(res_matrix)
        
        else:
            raise ArithmeticError('Operand is supposed to be int, \
                                  float or an instance of the Matrix class')
        
    def __matmul__(self, ent):
        
        if isinstance(ent, Matrix):

            n, m = len(self.matrix), len(self.matrix[0])
            d, k = len(ent.matrix), len(ent.matrix[0])

            assert d == m, "Matrix dimensions are incompatible"

            for line in self.matrix:
                assert len(line) == m, 'Matrix 1 has arbitrary dimensions'
            
            for line in ent.matrix:
                assert len(line) == k, 'Matrix 2 has arbitrary dimensions'        
            
            res_matrix = [[None] * k for _ in range(n)]

            # resulting matrix calculation
            for i in range(n): 
                for v in range(k):
                    for j in range(m):
                        res_matrix[i][v] += self.matrix[i][j] * ent.matrix[j][v]
            
            return Matrix(res_matrix)             
         
        else:
            raise ArithmeticError('Operand is supposed to be \
                                  an instance of the Matrix class')
