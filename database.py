import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = os.getenv("DATABASE_URL", "mysql+pymysql://root:NewPassword%40123@localhost/myproject")

if db_url.startswith("mysql://"):
    db_url = db_url.replace("mysql://", "mysql+pymysql://", 1)

engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)