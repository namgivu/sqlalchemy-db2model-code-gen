# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Integer, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, server_default=text("nextval('customers_id_seq'::regclass)"))
    name = Column(Text)
    dob = Column(Date)
    updated_at = Column(DateTime)
