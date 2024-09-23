from typing import Type
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ProductCreate, ProductUpdate
from core.models import Product


async def get_products(
        session: AsyncSession
) -> list[Product]:
    req = select(Product).order_by(Product.id)
    result: Result = await session.execute(req)
    products = result.scalars().all()
    return list(products)


async def create_product(
        session: AsyncSession,
        product_in: ProductCreate
) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    return product


async def get_product(
        session: AsyncSession,
        product_id: int
) -> Product | None:
    product = await session.get(Product, product_id)
    return product


async def update_product(
        session: AsyncSession,
        product_id: int,
        product_update: ProductUpdate,
) -> Type[Product] | None:
    product = await session.get(Product, product_id)
    if product is None:
        return product
    for name, value in product_update.model_dump(exclude_unset=False).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(
        session: AsyncSession,
        product_id: int
) -> bool:
    product = await session.get(Product, product_id)
    if product is None:
        return False
    await session.delete(product)
    await session.commit()
    return True


async def update_product_amount_by_id(
        session: AsyncSession,
        product_id: int,
        required_amount: int
) -> int | None:
    product = await get_product(session=session, product_id=product_id)
    if product is None or product.amount < required_amount:
        return None
    product.amount -= required_amount
    await session.commit()
    await session.refresh(product)
    return product.amount

