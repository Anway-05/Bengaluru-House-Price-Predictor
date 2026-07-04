from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/')
def home():
    return "Server is running"


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():

    location = request.form.get('location')
    total_sqft = float(request.form.get('total_sqft'))
    bhk = int(request.form.get('bhk'))
    bath = int(request.form.get('bath'))
    balcony = int(request.form.get('balcony'))

    estimated_price = util.get_estimated_price(
        location,
        total_sqft,
        bath,
        balcony,
        bhk
    )

    response = jsonify({
        'estimated_price': estimated_price
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Flask Server For Bengaluru House Price Prediction...")
    util.load_saved_artifacts()
    app.run(host="0.0.0.0", port=5000, debug=True)