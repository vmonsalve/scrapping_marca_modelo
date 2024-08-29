from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base 

class Modelo(Base):
    __tablename__ = 'modelos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    marca_id = Column(Integer, ForeignKey('marcas.id'), nullable=False)
    
    marca = relationship('Marca', back_populates='modelos')