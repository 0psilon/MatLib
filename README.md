# MATLIB

MatLib is a little python 2D-matrix-handling library. The following documentation will guide you through!

### Getting started:
```
pip install matlib
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

#[[1.0, 1.0]
# [1.0, 1.0]
# [1.0, 1.0]
# [1.0, 1.0]]
```
```
print(a + b) # +, -, *, /, //, %

#[[3.0, 3.0]
# [3.0, 3.0]
# [3.0, 3.0]
# [3.0, 3.0]]
```

```
print(a - 100) # +, -, *, /, //, %

#[[-99.0, -99.0]
# [-99.0, -99.0]
# [-99.0, -99.0]
# [-99.0, -99.0]]
```

```
a *= 2.5 # inplace
print(a)

#[[2.5, 2.5]
# [2.5, 2.5]
# [2.5, 2.5]
# [2.5, 2.5]]
```

### Exponentiation:
```
import matlib as ml

a = ml.Matrix([
    [2, 2],
    [2, 2]
])

print(a ** 3) # int

#[[32.0, 32.0]
# [32.0, 32.0]]
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

#[[12.0, 12.0, 12.0, 12.0]
# [12.0, 12.0, 12.0, 12.0]
# [12.0, 12.0, 12.0, 12.0]
# [12.0, 12.0, 12.0, 12.0]]
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

#[[2.0, 2.0, 2.0, 2.0]
# [2.0, 2.0, 2.0, 2.0]]
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

#[[12.0, 12.0, 12.0, 12.0]
# [12.0, 12.0, 12.0, 12.0]
# [12.0, 12.0, 12.0, 12.0]
# [12.0, 12.0, 12.0, 12.0]]
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

b = ml.pow(a, 3) # int
print(b) # float

#[[32.0, 32.0]
# [32.0, 32.0]]

```


