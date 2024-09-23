from datetime import datetime
from pydantic import BaseModel, ConfigDict, PositiveInt

from core.models.order import OrderStatus


class OrderBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    status: OrderStatus = OrderStatus.in_process


class OrderCreate(OrderBase):
    product_id: int
    date: datetime
    amount: PositiveInt


class OrderUpdateStatus(OrderBase):
    pass


class Order(OrderBase):
    id: int
    date: datetime
