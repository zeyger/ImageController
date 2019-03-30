from flask import Flask, request, jsonify
from pathlib import *
import base64
import subprocess

app = Flask(__name__)


@app.route('/submit_image/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.get_json()
    enc_image = content['image'].encode('utf-8')
    image = base64.b64decode(enc_image)
    with open(str(Path.home()) + '/project/input/image_' + uuid + '.jpg', 'wb+') as f:
        f.write(image)

    subprocess.call(['./transform_image.sh'])
    return jsonify({"uuid": uuid})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
