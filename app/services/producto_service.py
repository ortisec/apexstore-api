from app.repositories import producto_repo


async def listar_productos(db):
    return await producto_repo.get_all(db)


async def obtener_producto(db, producto_id: int):
    return await producto_repo.get_by_id(db, producto_id)
