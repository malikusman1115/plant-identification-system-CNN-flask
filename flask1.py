import keras
from keras.models import load_model
import cv2
import numpy as np
from flask import jsonify
from flask import Flask, make_response
from json import dumps
model=load_model('test3.h5')
import flask
from flask import Flask, render_template,request

app = flask.Flask(__name__)



# routes
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    img =Flask.request.args['img']
    model.compile(optimizer=keras.optimizers.Adam(lr=0.0001),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    img = cv2.imread(img)

    img = cv2.resize(img, (1024,768))
    img = np.reshape(img, [1, 128, 128, 3])

    classes = model.predict_classes(img)
    ind = np.argmax(classes)
    print(type(classes))
    classes = classes.tolist()
    cedrus_deodara = 'cedrus_deodara'
    ficus_carica = 'ficus_carica'
    malus_pumila = 'malus_pumila'
    morus_alba = 'morus_alba'
    morus_rubra = 'morus_rubra'
    prunus_serotina = 'prunus_serotina'
    print(classes)
    if ind == 0:
        results = cedrus_deodara
    elif ind == 1:
        results = ficus_carica
    elif ind == 2:
        results = malus_pumila
    elif ind == 3:
        results = morus_alba
    elif ind == 4:
        results = morus_rubra
    elif ind == 5:
        results = prunus_serotina



    else:
        results = "error"
    return render_template('index.html', pred=results)



def main():
    """Run the app."""
    app.run(host='localhost', port=8000)  # nosec


if __name__ == '__main__':
    main()