from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Marca(Base):
    __tablename__ = 'marcas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    url = Column(String(255))
    
    modelos = relationship('Modelo', back_populates='marca')
