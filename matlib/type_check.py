from pydantic import BaseModel


class MatrixCheck(BaseModel):
    matrix: list[list[float]]