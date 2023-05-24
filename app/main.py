from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

DATABASE_URL = "mysql+asyncmy://fastapi_user:fastapi.123@localhost:0/base_IOT"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ... definir tus modelos aquí ...
class User(BaseModel):
    user_id: int
    user_nickname: str
    user_name: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/usuarios/", response_model=None)
def read_items(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM usuarios"))
    usuarios = list(result)
    print(usuarios)
    return usuarios

