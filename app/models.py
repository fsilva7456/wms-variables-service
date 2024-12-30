from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Variable(Base):
    __tablename__ = "variables"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    value = Column(String(255), nullable=True)