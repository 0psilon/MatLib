def mul(matrix_1: list[list[float | int]],
        matrix_2: list[list[float | int]]
        ) -> list[list[float]]:
    
    n, m = len(matrix_1), len(matrix_1[0])
    d, k = len(matrix_2), len(matrix_2[0])

    assert d == m, "Matrix dimensions are incompatible"

    for line in matrix_1:
        assert len(line) == m, 'Matrix 1 has arbitrary dimensions'
    
    for line in matrix_2:
        assert len(line) == k, 'Matrix 2 has arbitrary dimensions'        
    
    matrix = [[0] * k for _ in range(n)]

    # resulting matrix calculation
    for i in range(n): 
        for v in range(k):
            for j in range(m):
                matrix[i][v] += matrix_1[i][j] * matrix_2[j][v]
    
    return matrix
