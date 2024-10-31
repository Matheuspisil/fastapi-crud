from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time

SQLALCHEMY_DATABASE_URL = "postgresql://vusht:150220@db:5432/fastapi_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

connected = False
while not connected:
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        connected = True
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        time.sleep(5)  
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
