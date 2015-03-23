from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello from Logan!"

app.run(debug=True, port=8000, host='localhost')