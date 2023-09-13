from pydantic import BaseModel


class MatrixCheck(BaseModel):
    matrix: list[list[float]]


class MatrixException(Exception):
    pass