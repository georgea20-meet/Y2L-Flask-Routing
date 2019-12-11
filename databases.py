from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))

def add_product(name, price, picture_link, description):
	Camera_01 = Product(
		name = name ,
		price = price ,
		picture_link = picture_link ,
		description = description)
	session.add(Camera_01)
	session.commit()

add_product("Nikon" , 12.000 , "htthttps://www.google.com/url?sa=i&url=https%3A%2F%2Fgadgets.ndtv.com%2Fcanon-eos-600d-18mp-dslr-camera-11670&psig=AOvVaw1BTS-JA_xgzDjto0z76YNQ&ust=1576166186537000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJCHheH6reYCFQAAAAAdAAAAABADhttps://www.google.com/url?sa=i&url=https%3A%2F%2Fgadgets.ndtv.com%2Fcanon-eos-600d-18mp-dslr-camera-11670&psig=AOvVaw1BTS-JA_xgzDjto0z76YNQ&ust=1576166186537000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJCHheH6reYCFQAAAAAdAAAAABADps://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bhphotovideo.com%2Fc%2Fproduct%2F1351688-REG%2Fnikon_d850_dslr_camera_body.html&psig=AOvVaw0A7KMAo48ykXpQVDP9atyB&ust=1576166024943000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLiHsJX6reYCFQAAAAAdAAAAABAJ" , "High quality DSLR" )

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

def update_price(their_id, price):
	Product = session.query(Product).filter_by(id = their_id).first()
	Product.price = price
	session.commit()

def Add_To_Cart(ProductID):
	add_1stproduct = Cart(
		ProductID = ProductID )
	session.add(add_1stproduct)
	session.commit()
