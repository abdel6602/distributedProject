from flask import Flask, jsonify, request, send_from_directory, send_file

app = Flask(__name__)

@app.route('/<id>')
def serve_image(id):
    return send_from_directory('/static/images', f'{id}.jpg')

@app.route('/<id>/processed', methods=['POST'])
def save_processed_image(id):
    image_data = request.get_data()
    with open(f'/static/images/{id}.jpg', 'wb') as f:
        f.write(image_data)
    return jsonify({'message': 'Image saved'})


if __name__ == '__main__':
    app.run(debug=True, port='8081')