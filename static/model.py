from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Student(Base):
   __tablename__ = 'students'
   product_id = Column(Integer, primary_key=True)
   name = Column(string)
   price = Column(float)
   picture_link = Column(string)
   description = Column(string)

class cart(Base):
   __tablename__ = 'productID'
   productID=Column(Integer,primary_key=True)
