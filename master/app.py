from flask import Flask, jsonify, request
import os
import master
import random
import string

app = Flask(__name__)

def random_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

@app.route('/')
def hello():
    return jsonify(message='Hello, World!')

@app.route('/process_image/<op>/<params>', methods=['POST'])
def process_image(op, params):
    if 'image' in request.files:
        image = request.files['image']
        image.save('./images/test.jpg')
        status, id = master.main('./images/test.jpg', operation=op, params=params, id=random_id())
        if status:
            response = {
                'message': 'Image processing task sent successfully.',
                'id': str(id)
            }
            return jsonify(response)
        else:
            return jsonify(message='No image file found.')
            


if __name__ == '__main__':
    app.run(debug=True)