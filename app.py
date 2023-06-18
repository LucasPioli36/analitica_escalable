from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import joblib

app = Flask(__name__, template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sex = request.form['sex']
        pclass = int(request.form['pclass'])
        age = float(request.form['age'])
        return redirect(url_for('result', sex=sex, pclass=pclass, age=age))
    return render_template('index.html')

@app.route('/result/<string:sex>/<int:pclass>/<float:age>', methods=['GET', 'POST'])
def result(sex, pclass, age):
    # Load the trained pipeline model
    pipeline = joblib.load("pipelineModel.pkl")

    # Create a DataFrame with the input values
    data = pd.DataFrame([[sex, pclass, age]], columns=['sex', 'pclass', 'age'])

    # Make predictions using the pipeline model
    prediction = pipeline.predict(data)[0]

    if prediction == 1:
        prediction = "Survived"
    else:
        prediction = "Not Survived"

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int("5000"))