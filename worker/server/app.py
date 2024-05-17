from flask import Flask, jsonify, request, send_from_directory, send_file

app = Flask(__name__)

@app.route('/<id>')
def serve_image(id):
    return send_from_directory('../static/images', f'{id}.jpg')

if __name__ == '__main__':
    app.run(debug=True, port='8081')