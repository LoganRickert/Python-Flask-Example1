from flask import Flask
from flask import request

app = Flask(__name__)

# Test URLs
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# http://localhost:8000/
# Produces 'Hello from Logan'
# http://localhost:8000/?name=Bob
# Produces 'Hello from Bob'

# Route is the everything after the http://~/
# route('index') = http://~/index
@app.route('/')
def index(name="Logan"):
	name = request.args.get('name', name) # If we get a name, great, if we don't, use the provided.
	return "Hello from {}".format(name)

app.run(debug=True, port=8000, host='localhost')