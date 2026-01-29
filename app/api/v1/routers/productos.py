from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db import get_db
from app.services import producto_service
from app.schemas.producto import ProductoBase, ProductoOut

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get("/", response_model=list[ProductoOut])
async def listar(db: AsyncSession = Depends(get_db)):
    return await producto_service.listar_productos(db)

@router.get("/{producto_id}", response_model=ProductoOut)
async def obtener(producto_id: int, db: AsyncSession = Depends(get_db)):
    producto = await producto_service.obtener_producto(db, producto_id)
    if not producto:
        raise HTTPException(404, "Producto no encontrado")
    return producto

@router.post("/", response_model=ProductoOut)
async def crear(data: ProductoBase, db: AsyncSession = Depends(get_db)):
    return await producto_service.crear_producto(db, data)


@router.put("/{producto_id}", response_model=ProductoOut)
async def actualizar(producto_id: int, data: ProductoBase, db: AsyncSession = Depends(get_db)):
    producto = await producto_service.obtener_producto(db, producto_id)
    if not producto:
        raise HTTPException(404, "Producto no encontrado")
    return await producto_service.actualizar_producto(db, producto, data)


@router.delete("/{producto_id}", status_code=204)
async def eliminar(producto_id: int, db: AsyncSession = Depends(get_db)):
    producto = await producto_service.obtener_producto(db, producto_id)
    if not producto:
        raise HTTPException(404, "Producto no encontrado")
    await producto_service.eliminar_producto(db, producto)
