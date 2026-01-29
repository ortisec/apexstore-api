from pydantic import BaseModel
from typing import List
from app.schemas.categoria import CategoriaOut
from app.schemas.imagen import ImagenProductoOut


class ProductoBase(BaseModel):
    nombre: str
    descripcion: str | None = None
    precio: float
    stock: int
    id_categoria: int


class ProductoOut(ProductoBase):
    id_producto: int
    categoria: CategoriaOut
    imagenes: List[ImagenProductoOut] = []

    class Config:
        from_attributes = True
