import database
from flask import Flask

app = Flask(__name__)
app.secret_key = 'Cibre70'

@app.route('/')