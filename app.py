import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask,request,app,jsonify,url_for,render_template

app=Flask(__name__)
model = tf.keras.models.load_model("churn.h5")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict():
    age = int(request.form['age'])
    gender = int(request.form['gender'])
    location = int(request.form['location'])
    subscription_length = int(request.form['subscription'])
    monthly_bill = float(request.form['bill'])
    total_usage = float(request.form['usage'])
    Bill_per_GB = float(total_usage/monthly_bill)
    Usage_Bill_Interaction = float(total_usage*monthly_bill)
    GBpermonth = float(total_usage/subscription_length)
    Subscrition_Value = float(total_usage/(subscription_length*monthly_bill))
    monthly_bill_cat = 0
    if monthly_bill>0 and monthly_bill<50:
        monthly_bill_cat = 0
    elif monthly_bill>50 and monthly_bill<100:
        monthly_bill_cat = 1
    else:
        monthly_bill_cat = 2
    Long_Term_Customer = 0
    if subscription_length>12:
        Long_Term_Customer = 1
    else:
        Long_Term_Customer = 0
    input_data = np.array([[age, gender, location, subscription_length, monthly_bill, total_usage,
                            Bill_per_GB, Usage_Bill_Interaction, GBpermonth, Subscrition_Value, monthly_bill_cat, Long_Term_Customer]])

    churn_prediction = model.predict(input_data)
    
    if churn_prediction > 0.5:
        result = "Churn"
    else:
        result = "No Churn"

    return render_template('result.html', result=result)
if __name__ == "__main__":
    app.run(debug=True, port=5001)






