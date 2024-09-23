from typing import Type
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import OrderItem, Order
from .schemas import OrderCreate, OrderUpdateStatus
from ..product.crud import update_product_amount_by_id


async def get_orders(
        session: AsyncSession
) -> list[Order]:
    req = select(Order).order_by(Order.id)
    result: Result = await session.execute(req)
    orders = result.scalars().all()
    return list(orders)


async def get_order(
        session: AsyncSession,
        order_id: int
) -> Order | None:
    return await session.get(Order, order_id)


async def create_order(
        session: AsyncSession,
        order_in: OrderCreate
) -> Order | None:
    order_in_dict = order_in.model_dump()

    product_id = order_in_dict.get('product_id')
    required_amount = order_in_dict.get('amount')
    product_amount = await update_product_amount_by_id(
        session=session,
        product_id=product_id,
        required_amount=required_amount
    )
    if product_amount is None:
        return None

    order = Order(
        date=order_in_dict.get('date'),
        status=order_in_dict.get('status')
    )
    session.add(order)
    await session.commit()
    await session.refresh(order)

    order_id = order.id
    order_item = OrderItem(
        order_id=order_id,
        product_id=product_id,
        amount=required_amount
    )
    session.add(order_item)
    await session.commit()
    return order


async def update_order_status(
        session: AsyncSession,
        order_id: int,
        order_update: OrderUpdateStatus
) -> Type[Order] | None:
    order = await session.get(Order, order_id)
    if order is None:
        return None
    order.status = order_update.status
    await session.commit()
    return order
