from app.models.producto import Producto
from app.repositories import producto_repo


async def listar_productos(db):
    return await producto_repo.get_all(db)


async def obtener_producto(db, producto_id: int):
    return await producto_repo.get_by_id(db, producto_id)


async def crear_producto(db, data):
    producto = Producto(**data.dict())
    return await producto_repo.create(db, producto)


async def actualizar_producto(db, producto, data):
    for field, value in data.dict().items():
        setattr(producto, field, value)
    await producto_repo.update(db)
    return producto


async def eliminar_producto(db, producto):
    await producto_repo.delete(db, producto)
