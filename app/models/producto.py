from sqlalchemy import String, ForeignKey, Numeric, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class Producto(Base):
    __tablename__ = "productos"
    __table_args__ = (CheckConstraint("stock >= 0"),)

    id_producto: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(150), nullable=False)
    descripcion: Mapped[str | None] = mapped_column(String(255))
    precio: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    stock: Mapped[int] = mapped_column(nullable=False)

    id_categoria: Mapped[int] = mapped_column(
        ForeignKey("categorias.id_categoria"),
        nullable=False,
    )

    categoria = relationship("Categoria", back_populates="productos")
    imagenes = relationship(
        "ImagenProducto",
        back_populates="producto",
        cascade="all, delete",
    )
