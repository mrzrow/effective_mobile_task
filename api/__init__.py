from fastapi import APIRouter

from core.config import settings
from .product.views import router as product_router
from .order.views import router as order_router

router = APIRouter(prefix=settings.api_prefix)
router.include_router(router=product_router)
router.include_router(router=order_router)
