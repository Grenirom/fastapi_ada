from settings import Base, engine
from apps.models import Product

# Создаем таблицы в бд
print("CREATING TABLE product")
Base.metadata.create_all(bind=engine)
print("DONE")