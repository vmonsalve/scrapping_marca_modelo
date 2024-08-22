from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Marca(Base):
    __tablename__ = 'marcas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)

    modelos = relationship('Modelo', back_populates='marca')