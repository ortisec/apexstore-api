from app.models.imagen import ImagenProducto
from app.repositories import imagen_repo

async def listar_imagenes(db):
    return await imagen_repo.get_all(db)

async def listar_imagenes_por_producto(db, producto_id: int):
    return await imagen_repo.get_by_producto_id(db, producto_id)


async def crear_imagen(db, data):
    imagen = ImagenProducto(**data.dict())
    return await imagen_repo.create(db, imagen)

async def actualizar_imagen(db, imagen, data):
    return await imagen_repo.update(db, imagen, data.dict())

async def eliminar_imagen(db, imagen):
    await imagen_repo.delete(db, imagen)
