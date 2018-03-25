from flask import Flask, request
#import the alphabet_position and rotate_character functions from the helpers module 
from helpers import alphabet_position, rotate_character
#import the rotate_string function from the caesar module 
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form ="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/encrypt" method="post">
             <label for="rot">Rotate by:</label>
            <input id="rot" type="text" name="rot" value=0 />
            <textarea name="text">{0}</textarea>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rotate = int(request.form["rot"])
    message = request.form["text"]

    encrypted_string = rotate_string(message, rotate)
    
    new_form = form.format(encrypted_string)

    return new_form

app.run()