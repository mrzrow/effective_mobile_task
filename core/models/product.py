from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base


class Product(Base):
    name: Mapped[str] = mapped_column(
        String(32),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        nullable=False
    )

    amount: Mapped[int] = mapped_column(
        nullable=False
    )

    order_items = relationship('OrderItem', back_populates='product')
