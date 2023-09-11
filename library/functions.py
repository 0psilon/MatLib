import matlib as ml
from check import MatrixException


def det(matrix: ml.Matrix) -> float:

    if not isinstance(matrix, ml.Matrix):
        raise MatrixException('Given matrix must be an instance of the Matrix class')

    n = len(matrix)
    
    for line in matrix:
        if len(line) != n:
            raise MatrixException('Given matrix is not a square matrix')

    counter = 0
    ans = 1.

    # checking if not a zero column
    for g in range(n): 
        if matrix[g][0] == 0:
            counter += 1

    if counter == n:
        ans = 0.

    # making a triangular matrix
    else:
        for rep in range(n - 1): 
            if matrix[rep][rep] == 0:
                for i in range(rep, n):
                    if matrix[i][rep] != 0: 
                        matrix[rep], matrix[i] = matrix[i], matrix[rep]
                        ans *= -1
                        break
                        
            for j in range(rep + 1, n):
                if matrix[j][rep] != 0:
                    coeff = matrix[j][rep] / matrix[rep][rep]
                    for k in range(rep, n):                
                        matrix[j][k] += (-1 * coeff * matrix[rep][k])

    # calculating triangular matrix determinant 
    # by multiplying the main diagonal values
    for i in range(n): 
        ans *= matrix[i][i]

    return ans


def mul(matrix_1: ml.Matrix,
        matrix_2: ml.Matrix
        ) -> ml.Matrix:
    
    if not isinstance(matrix_1, ml.Matrix):
        raise MatrixException('Given matrix must be an instance of the Matrix class')
    
    if not isinstance(matrix_2, ml.Matrix):
        raise MatrixException('Given matrix must be an instance of the Matrix class')

    n, m = len(matrix_1), len(matrix_1[0])
    d, k = len(matrix_2), len(matrix_2[0])

    if d != m:
        raise MatrixException('Matrix dimensions are incompatible')

    for line_1, line_2 in zip(matrix_1.matrix, matrix_2.matrix):
        if len(line_1) != m:
            raise MatrixException('Matrix 1 has arbitrary dimensions')
    
        if len(line_2) != k:
            raise MatrixException('Matrix 2 has arbitrary dimensions')
    
    res_matrix = [[0.] * k for _ in range(n)]

    # resulting matrix calculation
    for i in range(n): 
        for v in range(k):
            for j in range(m):
                res_matrix[i][v] += matrix_1[i][j] * matrix_2[j][v]
    
    return ml.Matrix(res_matrix)


def pow(matrix: ml.Matrix,
        exp: int = 1
        ) -> ml.Matrix:

    if not isinstance(matrix, ml.Matrix):
        raise MatrixException('Given matrix must be an instance of the Matrix class')
    
    if not isinstance(exp, int):
        raise TypeError('Exponent must be of the type integer')

    if exp <= 0:
        raise TypeError('Exponent must be positive')
    
    exp -= 1

    n = len(matrix)
    
    for line in matrix.matrix:
        if len(line) != n:
            raise MatrixException('Given matrix is not a square matrix')
    
    result = [[0.] * n for _ in range(n)]
    base = matrix.matrix.copy()

    while exp > 0:
        for i in range(n):
            for v in range(n):
                for j in range(n):
                    result[i][v] += base[i][j] * matrix[j][v]
        base = result.copy()
        result = [[0.] * n for _ in range(n)]
        exp -= 1
    
    return ml.Matrix(base)


def least_squares(matrix: ml.Matrix,
                  matrix_ans: ml.Matrix,
                  eps: float = 1e-6
                  ) -> ml.Matrix:
    
    if not isinstance(matrix, ml.Matrix):
        raise MatrixException('Given matrix must be an instance of the Matrix class')
    
    if not isinstance(matrix_ans, ml.Matrix):
        raise MatrixException('Given matrix must be an instance of the Matrix class')

    n, m = len(matrix), len(matrix[0])

    if len(matrix_ans) != n:
        raise MatrixException('Dimensions of matrices are incompatible')

    for line_1, line_2 in zip(matrix, matrix_ans):
        if len(line_1) != m:
            raise MatrixException('Matrix has arbitrary dimensions')
    
        if len(line_2) != 1:
            raise MatrixException('Matrix of answers has more than 1 value per line')

    result = []

    # создаем транспонированную матрицу векторов, заполненную нулями
    matrix_T = ml.Matrix([[0.] * n for _ in range(m)])
        
    # заполняем матрицы значениями
    for i in range(m):
        for j in range(n):
            matrix_T[i][j] = matrix[j][i]
            
    # перемножаем матрицы        
    a = mul(matrix_T, matrix)
    b = mul(matrix_T, matrix_ans)

    # создаем расширенную матрицу
    for i in range(len(a)):
        a[i].extend(b[i])
        
    # формируем верхнетругольную матрицу методом Гаусса     
    for rep in range(m):
        
        # переставляем местами строки, если начинаются с 0
        if abs(a[rep][rep]) < eps:  
            for i in range(rep, m):
                if abs(a[i][rep]) > eps: 
                    a[rep], a[i] = a[i], a[rep]
                    break

        # формируем верхнетреугольную матрицу
        for j in range(rep + 1, m): 
            if abs(a[j][rep]) > eps:
                coeff = a[j][rep] / a[rep][rep]
                for k in range(rep, m + 1):                
                    a[j][k] += -1 * coeff * a[rep][k]


    # решаем нормальную систему уравнений из m по m
    j, f = -1, -2
    for i in range(m - 1, 0, -1):
        x = a[i][j] / a[i][f]
        result.append(x)
                
        for v in range(len(result)):
            a[i - 1][j] += -1 * a[i - 1][m - 1 - v] * result[v]
        f -= 1
                    
    x = a[0][j] / a[0][f]
    result.append(x)
    result.reverse()
    
    return ml.Matrix([[x] for x in result])


def gaussian_elimination(matrix: ml.Matrix,
                         matrix_ans: ml.Matrix,
                         eps: float = 1e-6
                         ) -> ml.Matrix:
    
    if not isinstance(matrix, ml.Matrix):
        raise MatrixException('Given matrix must be an instance of the Matrix class')
    
    if not isinstance(matrix_ans, ml.Matrix):
        raise MatrixException('Given matrix must be an instance of the Matrix class')
    
    n, m = len(matrix), len(matrix[0])

    if len(matrix_ans) != n:
        raise MatrixException('Dimensions of matrices are incompatible')

    for line_1, line_2 in zip(matrix, matrix_ans):
        if len(line_1) != m:
            raise MatrixException('Matrix has arbitrary dimensions')
    
        if len(line_2) != 1:
            raise MatrixException('Matrix of answers has more than 1 value per line')
    
    matrix_w = [matrix[i].copy() for i in range(n)]

    for i in range(n):
        matrix_w[i].extend(matrix_ans[i])

    result = []

    for rep in range(min(m, n)):
        
        #переставляем местами строки, если начинаются с 0
        if abs(matrix_w[rep][rep]) < eps:  
            for i in range(rep, n):
                if abs(matrix_w[i][rep]) > eps: 
                    matrix_w[rep], matrix_w[i] = matrix_w[i], matrix_w[rep]
                    break

        #формируем верхнетреугольную матрицу
        for j in range(rep + 1, n): 
            if abs(matrix_w[j][rep]) > eps:
                coeff = matrix_w[j][rep] / matrix_w[rep][rep]
                for k in range(rep, m + 1):                
                    matrix_w[j][k] += -1 * coeff * matrix_w[rep][k]

    #определяем ранг расширенной матрицы
    counter1, counter2 = 0, 0 

    for i in matrix_w:
        for j in i:
            if abs(j) < eps:
                counter1 += 1

        if counter1 == m + 1:
            counter2 += 1
        counter1 = 0
                    
    rank1 = n - counter2

    #определяем ранг основной матрицы
    counter1, counter2 = 0, 0 

    for i in range(n):
        for j in range(m):
            if abs(matrix_w[i][j]) < eps:
                counter1 += 1
    
        if counter1 == m:
            counter2 += 1
    
        counter1 = 0

    rank2 = n - counter2

    #сравниваем ранги и определяем наличие корней
    if rank1 != rank2: 
        print('System of equations cannot be solved')
        
        return ml.Matrix([[]])
        
    else:
        if rank1 != m:
            print('System of equations has infinite amount of answers')
            
            return ml.Matrix([[]])
            
        else:            
            j, f = -1, -2
            for i in range(rank1 - 1, 0, -1):
                x = matrix_w[i][j] / matrix_w[i][f]
                result.append(x)
                for v in range(len(result)):
                    matrix_w[i - 1][j] += -1 * matrix_w[i - 1][m - 1 - v] * result[v]
                f -= 1
                    
            x = matrix_w[0][j] / matrix_w[0][f]
            result.append(x)
            result.reverse()

            return ml.Matrix([[x] for x in result])
