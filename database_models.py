from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
Base = declarative_base()
class Product(Base):
    
    __tablename__ = "product"
    
    
    id = Column(Integer,primary_key=True, index = True)
    name = Column(String(100))
    description = Column(String(255))
    price = Column(Float)
    quantity = Column(Integer)
    
    