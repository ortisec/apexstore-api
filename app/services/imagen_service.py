from app.repositories import imagen_repo


async def listar_imagenes_por_producto(db, producto_id: int):
    return await imagen_repo.get_by_producto_id(db, producto_id)
