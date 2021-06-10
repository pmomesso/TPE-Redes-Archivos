from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'hello world'

@app.route('/search_flow')
def search_flow():
	r = requests.get('http://host.docker.internal:8081/webapp')
	if r.status_code != 200:
		return "probe_success 0"
	r = requests.get('http://host.docker.internal:8081/webapp/searchResults?name=stranger')
	if r.status_code != 200:
		return "probe_success 0"
	return "probe_success 1"

@app.route('/login')
def login():
    return 'login'
