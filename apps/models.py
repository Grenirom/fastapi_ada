from settings import Base
from sqlalchemy import Column, Integer, String, Text, Numeric


# Создаем таблицу продукта в БД
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    quantity = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)

