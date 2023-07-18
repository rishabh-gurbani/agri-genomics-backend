from flask import Flask, request, jsonify
from height_prediction import predict as predict_height

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    query_sequence = request.form.get('query_sequence')
    # modelType = [request.form.get('MODEL')]

    prediction = predict_height(query_sequence)

    return jsonify({'Height': str(prediction)})


if __name__ == '__main__':
    app.run(debug=True)
