from typing import List
from fastapi import APIRouter, HTTPException

from .serializers import ProductCreateSerializer, ProductSerializer, ProductUpdateSerializer
from .models import Product
from settings import SessionLocal


db = SessionLocal()
router = APIRouter()


@router.get('/products', response_model=List[ProductSerializer])
def product_list():
    products = db.query(Product).all() # - ORM
    # SELECT * FROM product; - сырой запрос
    return products

@router.get('/products/{id}', response_model=ProductSerializer)
def product_detail(id: int):
    product = db.query(Product).get(id)
    if product is None:
        raise HTTPException(status_code=404, detail='Product not found')
    return product


@router.post('/products', status_code=201)
def create_product(data: ProductCreateSerializer):
    new_product = Product(
        title=data.title,
        price=data.price,
        quantity=data.quantity,
        description=data.description
    )
    db.add(new_product)
    db.commit()
    return {'message': 'Successfully created product!'}


@router.patch('/products/{id}', status_code=201)
def update_product(id: int, data:ProductUpdateSerializer):
    product = db.query(Product).get(id)
    if product is None:
        raise HTTPException(404, 'Product not found!')
    if data.title:
        product.title = data.title
    if data.price:
        product.price = data.price
    if data.description:
        product.description = data.description
    if data.quantity:
        product.quantity = data.quantity
    db.commit()
    return {'message': 'Successfully updated product'}

@router.delete('/products/{id}', status_code=204)
def delete_product(id: int):
    product = db.query(Product).get(id)
    if product is None:
        raise HTTPException(404, 'product not found!')
    db.delete(product)
    db.commit()
