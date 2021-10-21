from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle



app = Flask(__name__)

@app.route('/' , methods =['GET'])
@cross_origin()
def homepage():
    return render_template('index.html' )

@app.route('/predict', methods =['POST' , 'GET'])
@cross_origin()
def Prediction():
    if request.method == 'POST':
        try:
            rate_marriage = float(request.form['rate_marriage'])
            religious = float(request.form['religious'])
            age = float(request.form['age'])
            yrs_married =float(request.form['yrs_married'])
            children = float(request.form['children'])
            educ = float(request.form['educ'])
            Occupation = float(request.form['occupation'])
            Occupation_hus = float(request.form['occupation_husb'])
            if Occupation == 2.0:
                occ_2 = 1.0
                occ_3 =0
                occ_4 = 0
                occ_5 =0
                occ_6 =0

            elif Occupation == 3.0:
                occ_2 = 0
                occ_3 = 1.0
                occ_4 = 0
                occ_5 = 0
                occ_6 =0

            elif Occupation == 4.0:
                occ_2 = 0
                occ_3 = 0
                occ_4 = 1.0
                occ_5 = 0
                occ_6 =0

            elif Occupation == 5.0:
                occ_2 = 0
                occ_3 = 0
                occ_4 = 0
                occ_5 = 1.0
                occ_6 =0

            elif Occupation == 6.0:
                occ_2 = 0
                occ_3 = 0
                occ_4 = 0
                occ_5 = 0
                occ_6 = 1.0
            else:
                occ_2 = 0
                occ_3 = 0
                occ_4 = 0
                occ_5 = 0
                occ_6 = 0
            if Occupation_hus == 2.0:
                occ_husb_2 = 1.0
                occ_husb_3 =0
                occ_husb_4 = 0
                occ_husb_5 =0
                occ_husb_6 =0

            elif Occupation_hus == 3.0:
                occ_husb_2 = 0
                occ_husb_3 = 1
                occ_husb_4 = 0
                occ_husb_5 = 0
                occ_husb_6 =0

            elif Occupation_hus == 4.0:
                occ_husb_2 = 0
                occ_husb_3 = 0
                occ_husb_4 = 1.0
                occ_husb_5 = 0
                occ_husb_6 =0

            elif Occupation_hus == 5.0:
                occ_husb_2 = 0
                occ_husb_3 = 0
                occ_husb_4 = 0
                occ_husb_5 = 1.0
                occ_husb_6 =0

            elif Occupation_hus == 6.0:
                occ_husb_2 = 0
                occ_husb_3 = 0
                occ_husb_4 = 0
                occ_husb_5 = 0
                occ_husb_6 = 1.0
            else:
                occ_husb_2 = 0
                occ_husb_3 = 0
                occ_husb_4 = 0
                occ_husb_5 = 0
                occ_husb_6 = 0



            filename = 'logistic_assign1.pickle'
            load_model = pickle.load(open(filename, 'rb'))
            predictionans = load_model.predict([[occ_2,occ_3,occ_4,occ_5,occ_6,occ_husb_2,occ_husb_3,occ_husb_4,occ_husb_5,occ_husb_6,rate_marriage,age,yrs_married,children,religious,educ]])
            if predictionans == 1:
                prediction = 'atleast one affair'
                image = 'https://www.gannett-cdn.com/-mm-/65d832a4fc5e4d9e3093079d8f6e933bf5ac3edc/c=0-0-616-348/local/-/media/Montgomery/LivingWell/2014/08/20/1408552900000-cheating-w-620x349.jpg?auto=webp&format=pjpg&width=1200'
            else:
                prediction = 'No affair'
                image = 'data:image/jpeg;base64,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'

            return render_template('results.html' , prediction = prediction , image = image)

        except Exception as e:
            print('the exception msg is : ', e)
            return 'Something went wrong'
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)