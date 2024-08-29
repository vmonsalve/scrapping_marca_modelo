from sqlalchemy.orm import sessionmaker
from Models.base import engine
from Models.marca import Marca

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def insertar_marca(marca, href):

    session = SessionLocal()
    try:
        nueva_marca = Marca(nombre=marca, url=href)
        session.add(nueva_marca)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error al insertar la marca: {e}")
    finally:
        session.close()

def obtener_marcas():
    session = SessionLocal()
    marcas = session.query(Marca).all()
    return marcas

def obtener_marca(id):
    session = SessionLocal()
    marca = session.query(Marca).filter(Marca.id == id).first()
    return marca
    pass