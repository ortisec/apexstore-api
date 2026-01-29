from sqlalchemy import select
from app.models.imagen import ImagenProducto


async def get_all(db):
    result = await db.execute(select(ImagenProducto))
    return result.scalars().all()

async def get_by_id(db, imagen_id: int):
    result = await db.execute(
        select(ImagenProducto).where(ImagenProducto.id_imagen == imagen_id)
    )
    return result.scalar_one_or_none()


async def get_by_producto_id(db, producto_id: int):
    result = await db.execute(
        select(ImagenProducto)
        .where(ImagenProducto.id_producto == producto_id)
        .order_by(ImagenProducto.orden)
    )
    return result.scalars().all()


async def create(db, imagen: ImagenProducto):
    db.add(imagen)
    await db.commit()
    await db.refresh(imagen)
    return imagen

async def update(db, imagen: ImagenProducto, data: dict):
    for key, value in data.items():
        setattr(imagen, key, value)
    db.add(imagen)
    await db.commit()
    await db.refresh(imagen)
    return imagen


async def delete(db, imagen: ImagenProducto):
    await db.delete(imagen)
    await db.commit()
