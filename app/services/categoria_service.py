from app.repositories import categoria_repo


async def listar_categorias(db):
    return await categoria_repo.get_all(db)


async def obtener_categoria(db, categoria_id: int):
    return await categoria_repo.get_by_id(db, categoria_id)
