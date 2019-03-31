from flask import Flask, request, jsonify
from pathlib import *
import base64
import subprocess

app = Flask(__name__)


@app.route('/submit_image/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.get_json()

    # decode source image
    enc_image = content['image'].encode('utf-8')
    image = base64.b64decode(enc_image)

    # decode style image
    enc_style = content['style'].encode('utf-8')
    style = base64.b64decode(enc_style)


    # save images

    with open(str(Path.home()) + '/project/ImageController/input/image' + '.jpg', 'wb+') as f:
        f.write(image)

    with open(str(Path.home()) + '/project/ImageController/input/style' + '.jpg', 'wb+') as f:
        f.write(style)

     
    subprocess.Popen(['python3', 'handler.py'])
    
    return jsonify({"uuid": uuid})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



