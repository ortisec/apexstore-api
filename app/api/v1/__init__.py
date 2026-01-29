from fastapi import APIRouter
from app.api.v1.routers import categorias, productos, imagenes

router = APIRouter()

router.include_router(categorias.router)
router.include_router(productos.router)
router.include_router(imagenes.router)
