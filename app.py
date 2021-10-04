# importing the necessary dependencies
import pickle

from flask import Flask, render_template, request
from flask_cors import cross_origin
import flasgger

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Intercept = float(request.form['Intercept'])
            occ_2 = float(request.form['occ_2'])
            occ_3 = float(request.form['occ_3'])
            occ_4 = float(request.form['occ_4'])
            occ_5 = float(request.form['occ_5'])
            occ_6 = float(request.form['occ_6'])
            occ_husb_2 = float(request.form['occ_husb_2'])
            occ_husb_3 = float(request.form['occ_husb_3'])
            occ_husb_4 = float(request.form['occ_husb_4'])
            occ_husb_5 = float(request.form['occ_husb_5'])
            occ_husb_6 = float(request.form['occ_husb_6'])
            rate_marriage = float(request.form['rate_marriage'])
            children = float(request.form['children'])
            religious = float(request.form['religious'])
            age = float(request.form['age'])
            yrs_married = float(request.form['yrs_married'])
            educ = float(request.form['educ'])

            filename = 'model.pkl'
            loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict([Intercept,occ_2,occ_3,occ_4,occ_5,occ_6,occ_husb_2,occ_husb_3,occ_husb_4,occ_husb_5,occ_husb_6,rate_marriage,children,religious,age,yrs_married,educ])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction=prediction)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app
