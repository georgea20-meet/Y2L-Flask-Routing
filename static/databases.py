
from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_student(name, price, picture_link, description):

    student_object = Student(
        name=name,
        price=price,
        picture_link=picture_link,
        description=description)
    session.add(student_object)
    session.commit()

def update_lab_status(Product_id):

   student_object = session.query(
       Student).filter_by(
       Product_id=Product_id).first()
 
   session.commit()

def delete_student(Product_id):

   session.query(Student).filter_by(
       Product_id=Product_id).delete()
   session.commit()

def query_all():

   students = session.query(
      Student).all()
   return students


print(query_all())

def query_by_name(Product_id):

   student = session.query(
       Student).filter_by(
       Product_id=Product_id).first()
   return student

def Add_To_Cart(ProductID):
	cart_object=cart
	(ProductID=ProductID)
	    session.add(cart_object)
    	session.commit()



