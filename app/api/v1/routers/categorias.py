from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db import get_db
from app.services import categoria_service
from app.schemas.categoria import CategoriaBase, CategoriaOut

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.get("/", response_model=list[CategoriaOut])
async def listar(db: AsyncSession = Depends(get_db)):
    return await categoria_service.listar_categorias(db)

@router.get("/{categoria_id}", response_model=CategoriaOut)
async def obtener(categoria_id: int, db: AsyncSession = Depends(get_db)):
    categoria = await categoria_service.obtener_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(404, "Categoria no encontrada")
    return categoria


@router.post("/", response_model=CategoriaOut)
async def crear(data: CategoriaBase, db: AsyncSession = Depends(get_db)):
    return await categoria_service.crear_categoria(db, data)


@router.put("/{categoria_id}", response_model=CategoriaOut)
async def actualizar(categoria_id: int, data: CategoriaBase, db: AsyncSession = Depends(get_db)):
    categoria = await categoria_service.obtener_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(404, "Categoria no encontrada")
    return await categoria_service.actualizar_categoria(db, categoria, data)


@router.delete("/{categoria_id}", status_code=204)
async def eliminar(categoria_id: int, db: AsyncSession = Depends(get_db)):
    categoria = await categoria_service.obtener_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(404, "Categoria no encontrada")
    await categoria_service.eliminar_categoria(db, categoria)
