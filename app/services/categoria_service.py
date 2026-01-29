from app.models.categoria import Categoria
from app.repositories import categoria_repo


async def listar_categorias(db):
    return await categoria_repo.get_all(db)


async def obtener_categoria(db, categoria_id: int):
    return await categoria_repo.get_by_id(db, categoria_id)


async def crear_categoria(db, data):
    categoria = Categoria(**data.dict())
    return await categoria_repo.create(db, categoria)


async def actualizar_categoria(db, categoria, data):
    for field, value in data.dict().items():
        setattr(categoria, field, value)
    await categoria_repo.update(db)
    return categoria


async def eliminar_categoria(db, categoria):
    await categoria_repo.delete(db, categoria)
