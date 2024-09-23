from core.models.base import Base

from sqlalchemy import DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
import enum


class OrderStatus(str, enum.Enum):
    in_process = 'В процессе'
    sent = 'Отправлен'
    delivered = 'Доставлен'


class Order(Base):
    date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        Enum(OrderStatus)
    )

    order_items = relationship('OrderItem', back_populates='order')
