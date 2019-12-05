from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(Camera):
	Camera_01 = Product(
		type=type ,
		model=model ,
		price=price)
	session.add(Product)
	session.commit()

add_product("Nikon" , "D850" , 12000 )

def add_product(Camera):
	Camera_02 = Product(
		type=type ,
		model=model ,
		price=price)
	session.add(Product)
	session.commit()
	
add_product("Canon" , "600D" , 6500 )

def query_by_id(their_id):
	
	DSLR = session.query(Product).filter_by(id = their_id ).first()
	return DSLR

print(query_by_id("Nikon"))

def delete_product(their_name):
	session.query(Product).filter_by(name = their_name).delete()
	session.commit()
	
delete_product("Canon")

def query_all():
	products = session.query(Product).all()
	return products

print(query_all())

def update_price(their_price):
	Product = session_query(Product).filter_by(price = their_price).first()
	Product.price = price
	session.commit()

update_price( 14000 )

def Add_To_Cart(ProductID):
	Cart = Add_To_Cart
	session.add(Cart)
	session.commit()

print(query_all())