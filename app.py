import json
import pickle
import numpy as np
from flask import Flask,request,jsonify,render_template,url_for
import util
app=Flask(__name__)
models=['BMW', 'Bajaj', 'Benelli', 'Ducati', 'Harley-Davidson',
       'Hero', 'Honda', 'Hyosung', 'Ideal', 'Indian', 'Jawa', 'KTM',
       'Kawasaki', 'LML', 'MV', 'Mahindra', 'Rajdoot', 'Royal Enfield',
       'Suzuki', 'TVS', 'Triumph', 'Yamaha']
places=['24 Pargana', 'Agra',
       'Ahmedabad', 'Alibag', 'Alipore', 'Allahabad', 'Aurangabad',
       'Bangalore', 'Bhopal', 'Bhubaneshwar', 'Chandigarh', 'Chennai',
       'Coimbatore', 'Cuttack', 'Dehradun', 'Delhi', 'Ernakulam', 'Faridabad',
       'Gandhinagar', 'Gautam Buddha Nagar', 'Ghaziabad', 'Godhara',
       'Gorakhpur', 'Gurgaon', 'Guwahati', 'Howrah', 'Hyderabad', 'Indore',
       'Jaipur', 'Jalandhar', 'Jhansi', 'Jodhpur', 'Kadapa', 'Kalyan',
       'Kanchipuram', 'Kanpur', 'Karnal', 'Kolkata', 'Kota', 'Lucknow',
       'Ludhiana', 'Meerut', 'Mumbai', 'Nagpur', 'Nashik', 'Navi Mumbai',
       'Noida', 'Patna', 'Perumbavoor', 'Pune', 'Rajkot', 'Ranchi', 'Rohtak',
       'Rupnagar', 'Surat', 'Thane', 'Tiruvallur', 'Udaipur', 'Vadodara',
       'Visakhapatnam']
@app.route('/',methods=["GET","POST"])
def home():
    return render_template('index.html',title="home",models=models,places=places)

@app.route('/result',methods=["GET","POST"])
def result():
    return render_template('result.html')
@app.route("/predict_price",methods=["GET","POST"])

def predict_price():
    kms_driven=float(request.form["kms_drv"])
    city=request.form["place"]
    owner=int(request.form["owner"])
    age=int(request.form["age"])
    power=int(request.form["power"])
    brand=(request.form["model"])
    
    response=int(util.predict_prices(kms_driven,owner,age,power,city,brand))
    return render_template('result.html',result=response)
    


if __name__=="__main__":
    print("working")
    util.load_saved_artifacts()
    app.run(debug=True) 