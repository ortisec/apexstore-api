from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db import get_db
from app.services.imagen_service import listar_imagenes_por_producto
from app.schemas.imagen import ImagenProductoOut

router = APIRouter(prefix="/imagenes", tags=["Imagenes"])


@router.get("/producto/{producto_id}", response_model=list[ImagenProductoOut])
async def get_imagenes_por_producto(
    producto_id: int,
    db: AsyncSession = Depends(get_db),
):
    return await listar_imagenes_por_producto(db, producto_id)
