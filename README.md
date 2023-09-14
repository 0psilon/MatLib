# MATLIB

MatLib is a little python 2D-matrix-handling library. The following documentation will guide you through!

### Getting started:
```
pip install matlib

export n_digits=2 # precision: Optional[int], default is 3
```

## Standard operations:
```
import matlib as ml

a = ml.Matrix([
    [1, 1],
    [1, 1],
    [1, 1],
    [1, 1]
])

b = ml.Matrix([
    [2, 2],
    [2, 2],
    [2, 2],
    [2, 2]
])

print(a) # casting types

#[[1.00, 1.00]
# [1.00, 1.00]
# [1.00, 1.00]
# [1.00, 1.00]]
```
```
print(a + b) # +, -, *, /, //, %

#[[3.00, 3.00]
# [3.00, 3.00]
# [3.00, 3.00]
# [3.00, 3.00]]
```

```
print(a - 100) # +, -, *, /, //, %

#[[-99.00, -99.00]
# [-99.00, -99.00]
# [-99.00, -99.00]
# [-99.00, -99.00]]
```

```
a *= 2.5 # inplace
print(a)

#[[2.50, 2.50]
# [2.50, 2.50]
# [2.50, 2.50]
# [2.50, 2.50]]
```

### Exponentiation:
```
import matlib as ml

a = ml.Matrix([
    [2, 2],
    [2, 2]
])

print(a ** 3) # int

#[[32.00, 32.00]
# [32.00, 32.00]]
```

### Matrix multiplication:
```
import matlib as ml

a = ml.Matrix([
    [2, 2],
    [2, 2],
    [2, 2],
    [2, 2]
])

b = ml.Matrix([
    [3, 3, 3, 3],
    [3, 3, 3, 3]
])

print(a @ b)

#[[12.00, 12.00, 12.00, 12.00]
# [12.00, 12.00, 12.00, 12.00]
# [12.00, 12.00, 12.00, 12.00]
# [12.00, 12.00, 12.00, 12.00]]
```

### Transponing:
```
import matlib as ml

a = ml.Matrix([
    [2, 2],
    [2, 2],
    [2, 2],
    [2, 2]
])

print(a.T)

#[[2.00, 2.00, 2.00, 2.00]
# [2.00, 2.00, 2.00, 2.00]]
```

### Getting the size:
```
import matlib as ml

a = ml.Matrix([
    [2, 2],
    [2, 2],
    [2, 2],
    [2, 2]
])

print(a.size)

#(4, 2)
```

## The functions:

#### 1. Calculating the determinant of the matrix:

**func:** det(*matrix: ml.Matrix*) -> *float*

```
import matlib as ml

a = ml.Matrix([
    [2, 2],
    [2, 2]
])

b = ml.det(a)
print(b)

# 0.0
```

#### 2. Matrix multiplication:
**func:** mul(*matrix_1: ml.Matrix,
               matrix_2: ml.Matrix*
               ) -> *ml.Matrix*

```
import matlib as ml

a = ml.Matrix([
    [2, 2],
    [2, 2],
    [2, 2],
    [2, 2]
])

b = ml.Matrix([
    [3, 3, 3, 3],
    [3, 3, 3, 3]
])

c = ml.mul(a, b)
print(c)

#[[12.00, 12.00, 12.00, 12.00]
# [12.00, 12.00, 12.00, 12.00]
# [12.00, 12.00, 12.00, 12.00]
# [12.00, 12.00, 12.00, 12.00]]
```

#### 3. Matrix exponentiation:
**func:** pow(*matrix: ml.Matrix,
              exp: int = 1*
              ) -> *ml.Matrix*
```
import matlib as ml

a = ml.Matrix([
    [2, 2],
    [2, 2]
])

b = ml.pow(a, 3)
print(b)

#[[32.00, 32.00]
# [32.00, 32.00]]

```

#### 4. Mqtrix transposing:
**func:** transpose(*matrix: ml.Matrix*) -> *ml.Matrix*
```
import matlib as ml

a = ml.Matrix([
    [2, 2],
    [2, 2],
    [2, 2],
    [2, 2]
])

b = transpose(a)
print(b)

#[[2.00, 2.00, 2.00, 2.00]
# [2.00, 2.00, 2.00, 2.00]]
```

#### 5. Least Squares method:

**func:** least_squares(*matrix: ml.Matrix,
                        matrix_ans: ml.Matrix*
                        ) -> *ml.Matrix*

Finds an approximate solution for a system of linear equations.

```
import matlib as ml

a = ml.Matrix([
    [1, 1],
    [2, 1],
    [1, 5],
    [4, 1]
])

b = ml.Matrix([    
    [1],
    [4],
    [3],
    [7]
])

c = ml.least_squares(a, b)
print(c)

#[[1.69]
# [0.24]]
```

#### 6. Gaussian Elimination method:

**func:** gaussian_elimination(*matrix: ml.Matrix,
                                matrix_ans: ml.Matrix*
                                ) -> *ml.Matrix*

Solves a system of linear equations using the Gaussian Elimination method. The program responds whether the answer to the system exists, does not exist or is an infinite amount of answers.

```
import matlib as ml

a = ml.Matrix([
    [3, 1, -2, 1],
    [2, 3, -1, 2],
    [1, -2, 2, -1],
    [1, 3, -1, 1]
    
])

b = ml.Matrix([
    [5],
    [4],
    [4],
    [0]
])

c = ml.gaussian_elimination(a, b)
print(c)

#[[ 2.00]
# [-1.00]
# [ 1.00]
# [ 2.00]]

print(a @ c) # checking the answer

#[[5.00]
# [4.00]
# [4.00]
# [0.00]]
```

```
a = ml.Matrix([
    [2, -4],
    [-3, 6],
])

b = ml.Matrix([
    [-1],
    [2]
])

c = gaussian_elimination(a, b)
print(c)

#System of equations cannot be solved
#[[]]
```