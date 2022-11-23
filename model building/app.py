import flask
from flask import request,render_template
from flask_cors import CORS
import joblib
app=flask.Flak(__name__,static_url_path='')
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
        cfl=joblib.load(RFC.pkl)
        species=clf.predict(X)[0]
        return render_template('predict.html',predict=species)

    if __name__=='__main__':
        app.run()
               
               





