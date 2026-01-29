from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db import get_db
from app.services import imagen_service
from app.repositories import imagen_repo
from app.schemas.imagen import ImagenProductoCreate, ImagenProductoOut

router = APIRouter(prefix="/imagenes", tags=["Imagenes"])

@router.get("/", response_model=list[ImagenProductoOut])
async def listar(db: AsyncSession = Depends(get_db)):
    return await imagen_service.listar_imagenes(db)

@router.get("/producto/{producto_id}", response_model=list[ImagenProductoOut])
async def listar(producto_id: int, db: AsyncSession = Depends(get_db)):
    return await imagen_service.listar_imagenes_por_producto(db, producto_id)


@router.post("/", response_model=ImagenProductoOut)
async def crear(data: ImagenProductoCreate, db: AsyncSession = Depends(get_db)):
    return await imagen_service.crear_imagen(db, data)

@router.put("/{imagen_id}", response_model=ImagenProductoOut)
async def actualizar(imagen_id: int, data: ImagenProductoCreate, db: AsyncSession = Depends(get_db)):
    imagen = await imagen_repo.get_by_id(db, imagen_id)
    if not imagen:
        raise HTTPException(404, "Imagen no encontrada")
    return await imagen_service.actualizar_imagen(db, imagen, data)


@router.delete("/{imagen_id}", status_code=204)
async def eliminar(imagen_id: int, db: AsyncSession = Depends(get_db)):
    imagen = await imagen_repo.get_by_id(db, imagen_id)
    if not imagen:
        raise HTTPException(404, "Imagen no encontrada")
    await imagen_service.eliminar_imagen(db, imagen)
