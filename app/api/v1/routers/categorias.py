from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db import get_db
from app.services.categoria_service import listar_categorias, obtener_categoria
from app.schemas.categoria import CategoriaOut

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.get("/", response_model=list[CategoriaOut])
async def get_categorias(db: AsyncSession = Depends(get_db)):
    return await listar_categorias(db)


@router.get("/{categoria_id}", response_model=CategoriaOut)
async def get_categoria(categoria_id: int, db: AsyncSession = Depends(get_db)):
    categoria = await obtener_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria
