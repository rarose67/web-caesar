from flask import Flask, request

#import the alphabet_position and rotate_character functions from the helpers module 
from helpers import alphabet_position, rotate_character

#import the rotate_string function from the caesar module 
from caesar import rotate_string

import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rotate = int(request.form["rot"])
    message = request.form["text"]

    encrypted_string = rotate_string(message, rotate)
    
    template = jinja_env.get_template('form.html')
    return template.render(message=encrypted_string)

app.run()