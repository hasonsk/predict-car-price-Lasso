from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load("checkpoint/LinearRegressor.ckpt")
products = pd.read_csv("dataset/company.csv")["Name"].tolist()
input_data = pd.read_csv('dataset/input.csv')

@app.route("/", methods=["GET", "POST"])
def index():
    data_input = input_data.copy()
    if request.method == "POST":
        try:
            name = request.form["name"]
            year = int(request.form["year"])
            engine_cc = float(request.form["engine_cc"])
            power_bhp = float(request.form["power_bhp"])
            seats = int(request.form["seats"])

            Company = name.split()[0].lower()
            Company = f"Company_{Company}"
            Model = "Model_" + " ".join(name.split()[:2]).lower()

            data_input['Year'] = year
            data_input['Engine_CC'] = engine_cc
            data_input['Power_bhp'] = power_bhp
            data_input['Seats'] = seats
            data_input[Company] = 1
            data_input[Model] = 1

            # Predict the price using the model
            predicted_price = model.predict(data_input)[0]
            return render_template("result.html", predicted_price=predicted_price)
        
        except ValueError as err:
            error_message = str(err)
            return render_template("index.html", error_message=error_message)

    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
