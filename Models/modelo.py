
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Modelo(Base):
    __tablename__ = 'modelos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    marca_id = Column(Integer, ForeignKey('marcas.id'))

    marca = relationship('Marca', back_populates='modelos')
    bases = relationship('Base', back_populates='modelo')