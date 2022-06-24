# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

from flask import Flask
from flask import redirect

# Flask constructor takes the name of
# current module (__name__) as argument.

app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'rvce.edu.in'
@app.route('/rv')
def rvce():
  return 'RVCE ROCKS'
app.add_url_rule('/', 'rvce', rvce)


@app.route('/hello')
def hello():
	return redirect("http://www.rvce.edu.in", code=302)


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
