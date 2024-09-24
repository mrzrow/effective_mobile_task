# from fastapi.testclient import TestClient
# from main import app
#
# client = TestClient(app)
#
#
# def test_get_product_by_nonexistent_id():
#     response = client.get('/products/-1/')
#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Product not found'}
#
#
# def test_get_product_by_id():
#     response = client.get('/products/1/')
#     assert response.status_code == 200
#     assert response.json() == {
#         "name": "Молоко",
#         "description": "Дает корова",
#         "price": 120,
#         "amount": 8,
#         "id": 1
#     }

import pytest
from httpx import AsyncClient
from main import app


@pytest.mark.asyncio
async def test_get_product_by_nonexistent_id():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get('/products/-1/')
        assert response.status_code == 404
        assert response.json() == {'detail': 'Product not found'}


@pytest.mark.asyncio
async def test_get_product_by_id():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get('/products/1/')
        assert response.status_code == 200
        assert response.json() == {
            "name": "Молоко",
            "description": "Дает корова",
            "price": 120,
            "amount": 8,
            "id": 1
        }
