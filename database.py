from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
db_url = "mysql+pymysql://root:NewPassword%40123@localhost/myproject"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush=False, bind = engine)