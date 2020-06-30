

import numpy as np 
from flask import Flask,request,jsonify, render_template
import pickle

app=Flask(__name__)

model = pickle.load(open('catboost_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def predict():
    values = [int(each) for each in request.form.values()]
    result = model.predict(values)
    message=''
    if result==1:
        message = 'Congratulations!! Your request for access has been approved.'
    else:
        message = 'Sorry, your request for approval is rejected.Please contact your manager.'
    return render_template('result.html',prediction=message)

if __name__ =="__main__":
    app.run(debug=True)

    
