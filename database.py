import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

load_dotenv()

db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)