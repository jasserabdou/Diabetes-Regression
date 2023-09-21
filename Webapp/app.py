import numpy as np
import pickle as p
from sklearn.preprocessing import StandardScaler
from flask import Flask, render_template, request

mean_factors = np.array([48.51809954751131, 1.4683267118863047, 26.37579185520364, 94.64701357466063, 189.14027149321267, 49.788361490841054, 207.63243531202435, 4.070248858447488, 91.26018099358693, 4.641543612608034])
std_factors = np.array([13.109027717057796, 0.49956142697883553, 4.418121781769573, 13.831283589584983, 34.60805195184082, 11.343821437921673, 26.252347638186045, 0.2926947894894721, 16.97690652188136, 0.5228598213602433])


scaler = StandardScaler()
scaler.mean_ = mean_factors
scaler.scale_ = std_factors * np.sqrt(442)

app = Flask(__name__)
filename = "models/rf_model.pickle"


with open(filename, 'rb') as file:
    loaded_model = p.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    age = float(request.form['age'])
    sex = float(request.form['sex'])
    bmi = float(request.form['bmi'])
    bp = float(request.form['bp'])
    s1 = float(request.form['s1'])
    s2 = float(request.form['s2'])
    s3 = float(request.form['s3'])
    s4 = float(request.form['s4'])
    s5 = float(request.form['s5'])
    s6 = float(request.form['s6'])
    
    
    input_data = np.array([[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]])
    scaled_input = scaler.transform(input_data)

    
    prediction = loaded_model.predict(scaled_input)
    
    return render_template('predict.html', prediction=prediction)


if __name__ == '__main__':
    app.run()
