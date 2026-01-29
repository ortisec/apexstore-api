from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db import get_db
from app.services.producto_service import listar_productos, obtener_producto
from app.schemas.producto import ProductoOut

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get("/", response_model=list[ProductoOut])
async def get_productos(db: AsyncSession = Depends(get_db)):
    return await listar_productos(db)


@router.get("/{producto_id}", response_model=ProductoOut)
async def get_producto(producto_id: int, db: AsyncSession = Depends(get_db)):
    producto = await obtener_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto
