from flask import Flask, render_template, request
import utils

app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST']) 
def predict(): 
    if request.method == 'POST': 
        SepalLengthCm = request.form.get('SepalLengthCm')
        SepalWidthCm = request.form.get('SepalWidthCm')
        PetalLengthCm = request.form.get('PetalLengthCm')
        PetalWidthCm = request.form.get('PetalWidthCm') 
    prediction = utils.preprocessdata(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm) 

    return render_template('predict.html', prediction=prediction) 
if __name__ == '__main__': 
    app.run(debug=True) 

