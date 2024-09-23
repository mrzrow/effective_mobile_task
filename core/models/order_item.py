from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base


class OrderItem(Base):
    order_id: Mapped[int] = mapped_column(
        ForeignKey('order.id'),
        unique=False,
        nullable=False
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey('product.id'),
        unique=False,
        nullable=False
    )

    amount: Mapped[int] = mapped_column(
        nullable=False
    )

    order = relationship('Order', back_populates='order_items')

    product = relationship('Product', back_populates='order_items')
