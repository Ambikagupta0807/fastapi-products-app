from fastapi import Depends, FastAPI
from models import Product
from fastapi.middleware.cors import CORSMiddleware
from database import session, engine
import database_models
from sqlalchemy.orm import Session 
app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)
@app.get("/")
def greet():
    return "Welcome"
products = [
    Product(id=1, name = "Mobile", description ="budget phone", price = 99, quantity=10),
    Product(id=2, name = "Laptop", description ="gaming pc", price = 999, quantity=6),
    Product(id=3, name = "Watch", description ="digital watch", price = 80, quantity=40),
    Product(id=4, name = "Table", description ="Folding table", price =9, quantity=20) 
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    existing = db.query(database_models.Product).first()   # check karo table khali hai ya nahi
    if not existing:                                          # agar khali hai, tabhi insert karo
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
    db.close()
init_db()
@app.get("/products")
def get_all_pro(db : Session = Depends(get_db)):
    
    db_products = db.query(database_models.Product).all()
    
    return db_products

@app.get("/products/{id}")
def get_product_by_id (id:int, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "product not found"
        

@app.post("/products")
def add_product(product : Product, db : Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id:int , product : Product, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return
    else:
        return "No product found"
           
@app.delete("/products/{id}")
def delete_product(id:int, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    
    if db_product :
         db.delete(db_product)
         db.commit()
    else:
        return "Product not found"