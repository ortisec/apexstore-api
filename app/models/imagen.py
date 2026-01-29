from sqlalchemy import ForeignKey, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class ImagenProducto(Base):
    __tablename__ = "imagenes_producto"

    id_imagen: Mapped[int] = mapped_column(primary_key=True)
    url_imagen: Mapped[str] = mapped_column(Text, nullable=False)
    es_principal: Mapped[bool] = mapped_column(Boolean, default=False)
    orden: Mapped[int] = mapped_column(default=1)

    id_producto: Mapped[int] = mapped_column(
        ForeignKey("productos.id_producto"),
        nullable=False,
    )

    producto = relationship("Producto", back_populates="imagenes")
