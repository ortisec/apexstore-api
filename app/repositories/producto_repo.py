from sqlalchemy import select
from sqlalchemy.orm import joinedload
from app.models.producto import Producto


async def get_all(db):
    result = await db.execute(
        select(Producto).options(
            joinedload(Producto.categoria),
            joinedload(Producto.imagenes),
        )
    )
    return result.scalars().all()


async def get_by_id(db, producto_id: int):
    result = await db.execute(
        select(Producto)
        .where(Producto.id_producto == producto_id)
        .options(
            joinedload(Producto.categoria),
            joinedload(Producto.imagenes),
        )
    )
    return result.scalar_one_or_none()


async def create(db, producto: Producto):
    db.add(producto)
    await db.commit()
    await db.refresh(producto)
    return producto


async def update(db):
    await db.commit()


async def delete(db, producto: Producto):
    await db.delete(producto)
    await db.commit()
