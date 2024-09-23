from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Product, ProductCreate, ProductUpdate
from core.models import db_helper

router = APIRouter(tags=['Products'], prefix='/products')


@router.get('/', response_model=list[Product])
async def get_products(
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_products(session=session)


@router.post('/', response_model=Product)
async def create_product(
        product_in: ProductCreate,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get('/{product_id}/', response_model=Product)
async def get_product_by_id(
        product_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    product = await crud.get_product(session=session, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail='Product not found')
    return product


@router.put('/{product_id}/', response_model=Product)
async def update_product_by_id(
        product_id: int,
        product_update: ProductUpdate,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    product = await crud.update_product(
        session=session,
        product_id=product_id,
        product_update=product_update
    )
    if product is None:
        raise HTTPException(status_code=404, detail='Product not found')
    return product


@router.delete('/{product_id}/', response_model=None)
async def delete_product_by_id(
        product_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    result = await crud.delete_product(session=session, product_id=product_id)
    if not result:
        raise HTTPException(status_code=404, detail='Product not found')
