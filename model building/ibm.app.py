import flask
from flask import request,render_template
from flask_cors import CORS
import requests
API_KEY="6cLwgnZ5wAuI-j4vInDsaP0qkoede4XL80YMAWTyTMnE"
token_response=requests.post('https://iam.cloud.ibm.com/identity/token',data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app=flask.Flask(__name__,static_url_path='')
CORS(app)
@app.route('/',methods=['GET'])
def sendHomePage():
    return render_template(index.html)
    @app.route('predict',methods=['POST'])
    def predictSpecies():
        
        li= float(request.form['li'])
        na= float(request.form['na'])
        ge= float(request.form['ge'])
        ma= float(request.form['ma'])
        de= float(request.form['de'])
        ed= float(request.form['ed'])
        se= float(request.form['se'])
        ai= float(request.form['ai'])
        ca= float(request.form['ca'])
        la= float(request.form['la'])
        lat= float(request.form['lat'])
        ch= float(request.form['ch'])
        pa= float(request.form['pa'])
        ls= float(request.form['ls'])
        X=[[li,na,ge,ma,de,ed,se,ai,ca,la,lat,ch,pa,ls]]
        
        
        payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}

       response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/811e5422-ae26-4a71-879b-84159119f30a/predictions?version=2022-11-18', json=payload_scoring,
       headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
        predictions =response_scoring.json()
        predict= predictions['predictions'][0]['values'][0][0]
        print("Final Prediction:",predict)
        cfl=joblib.load(RFC.pkl)
        species=clf.predict(X)[0]
        return render_template('predict.html',predict=predict)

    if __name__=='__main__':
        app.run(debug = False)
               
               





