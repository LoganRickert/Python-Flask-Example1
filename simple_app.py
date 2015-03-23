from flask import Flask
# from flask import request
from flask import render_template

app = Flask(__name__)

# Test URLs
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# http://localhost:8000/
# Produces 'Hello from Logan'
# http://localhost:8000/Bob
# Produces 'Hello from Bob'
# http://localhost:8000/add/5/5
# Produces 10
# http://localhost:8000/add/5/a
# Produces a 404

# Route is the everything after the http://~/
# route('index') = http://~/index
# <name> is a GET request that provides a clean URL.
@app.route('/')
@app.route('/<name>')
def index(name="Logan"):
	# Remvoed because the /<name> does this for us now.
	# name = request.args.get('name', name) # If we get a name, great, if we don't, use the provided.
	return render_template("index.html", name=name)

# You can convert things into ints inside the URL
# A problem is that this produces a 404 if an integer is not provided.
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
def add(num1, num2):
	# Could also do this:
	# context = {'num1': num1, 'num2': num2}
	# return render_template("add.html", **context)
	return render_template("add.html", num1=num1, num2=num2)

# Runs the app in debug mode. The server will restart after each save automatically.
app.run(debug=True, port=8000, host='localhost')