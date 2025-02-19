from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *
app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route('/')
def homepage():
	return render_template("home.html")

@app.route('/store')
def store():
	Product = query_all()
	return render_template("store.html" , Product = Product)

@app.route('/cart')
def cart():
	return render_template("cart.html")

@app.route('/About')
def about():
	return render_template("about.html")

@app.route('/login' , methods=['GET','POST'])
def login():
	if request.method==GET :
		return 'You just made a GET request'
	else:
	return 'You just made a POST request'

@app.route('/portal')
def portal():
	return render_template("portal.html")


#####################


if __name__ == '__main__':
    app.run(debug=True)