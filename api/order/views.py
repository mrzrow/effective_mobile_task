from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Order, OrderCreate, OrderUpdateStatus
from core.models import db_helper

router = APIRouter(tags=['Orders'], prefix='/orders')


@router.get('/', response_model=list[Order])
async def get_orders(
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_orders(session=session)


@router.post('/', response_model=Order)
async def create_order(
        order_in: OrderCreate,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    order = await crud.create_order(session=session, order_in=order_in)
    if order is None:
        raise HTTPException(status_code=404, detail='Product not found or its amount is less than required')
    return order


@router.get('/{order_id}/', response_model=Order)
async def get_order_by_id(
        order_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    order = await crud.get_order(session=session, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail='Order not found')
    return order


@router.patch('/{order_id}/status', response_model=Order)
async def update_order_status_by_id(
        order_id: int,
        order_update: OrderUpdateStatus,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    order = await crud.update_order_status(
        session=session,
        order_id=order_id,
        order_update=order_update
    )
    if order is None:
        raise HTTPException(status_code=404, detail='Order not found')
    return order
