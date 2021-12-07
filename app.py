import logging
import pathlib
import pickle

from flask import Flask, request
from flask_cors import CORS
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import data

data.path.append(f'{pathlib.Path().resolve()}/nltk_data')
logging.getLogger().setLevel(logging.DEBUG)
app = Flask(__name__)

CORS(app)
app.debug = True


@app.route('/application', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        application = request.get_json().get("application", "")
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(application)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        singles = ' '.join([lemmatizer.lemmatize(plural).upper() for plural in filtered_sentence])

        loaded_model = pickle.load(open('classifiers/finalized_model.sav', 'rb'))
        pred = loaded_model.predict([singles])
        pred = int(pred[0])

        if pred == 0:
            result = 'GAMBLING'
        elif pred == 1:
            result = 'HUMAN TRAFFICKING'
        elif pred == 2:
            result = 'NON-CRIMINAL'
        elif pred == 3:
            result = 'PUBLIC INDECENCY'
        elif pred == 4:
            result = 'NARCOTICS'
        elif pred == 5:
            result = 'NON-CRIMINAL (SUBJECT SPECIFIED)'
        elif pred == 6:
            result = 'MOTOR VEHICLE THEFT'
        elif pred == 7:
            result = 'DECEPTIVE PRACTICE'
        elif pred == 8:
            result = 'OTHER OFFENSE'
        elif pred == 9:
            result = 'THEFT'
        elif pred == 10:
            result = 'HOMICIDE'
        elif pred == 11:
            result = 'ARSON'
        elif pred == 12:
            result = 'PUBLIC PEACE VIOLATION'
        elif pred == 13:
            result = 'INTIMIDATION'
        elif pred == 14:
            result = 'CONCEALED CARRY LICENSE VIOLATION'
        elif pred == 15:
            result = 'PROSTITUTION'
        elif pred == 16:
            result = 'CRIM SEXUAL ASSAULT'
        elif pred == 17:
            result = 'KIDNAPPING'
        elif pred == 18:
            result = 'STALKING'
        elif pred == 19:
            result = 'OTHER NARCOTIC VIOLATION'
        elif pred == 20:
            result = 'BATTERY'
        elif pred == 21:
            result = 'ASSAULT'
        elif pred == 22:
            result = 'BURGLARY'
        elif pred == 23:
            result = 'CRIMINAL TRESPASS'
        elif pred == 24:
            result = 'ROBBERY'
        elif pred == 25:
            result = 'INTERFERENCE WITH PUBLIC OFFICER'
        elif pred == 26:
            result = 'CRIMINAL DAMAGE'
        elif pred == 27:
            result = 'OFFENSE INVOLVING CHILDREN'
        elif pred == 28:
            result = 'SEX OFFENSE'
        elif pred == 29:
            result = 'OBSCENITY'
        elif pred == 30:
            result = 'NON - CRIMINAL'
        elif pred == 31:
            result = 'WEAPONS VIOLATION'
        elif pred == 32:
            result = 'LIQUOR LAW VIOLATION'
        else:
            result = 'OTHER'

        return {"result": result}

app.run(host="0.0.0.0")
