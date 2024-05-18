from flask import Flask, jsonify, request, send_from_directory, send_file
import pymongo

app = Flask(__name__)

@app.route('/<id>')
def serve_image(id):
    # Retrieve image from database
    image = pymongo.MongoClient('mongodb://34.155.67.189:27017')["focusSnap"]['processed_images'].find_one({'id': id})["image"]
    print(len(image))
    with open(f'./static/images/{id}.jpg', 'wb') as f:
        f.write(image)
    return send_from_directory('static/images', f'{id}.jpg')


if __name__ == '__main__':
    app.run(debug=True, port='8081')