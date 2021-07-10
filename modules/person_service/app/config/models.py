from __future__ import annotations
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String

BaseModel = declarative_base()


class Person(BaseModel):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
