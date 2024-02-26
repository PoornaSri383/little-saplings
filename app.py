from flask import Flask, render_template, jsonify, request, Markup
from model import predict_image
import utils

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)
            print('prediction', prediction)
            res = Markup(utils.disease_dic[prediction])
            print(res)
            return render_template('display.html', status=200, result=res)
        except Exception as e:
            import traceback
            print(f"Exception: {str(e)}")
            traceback.print_exc()
            print('geewf')
            return render_template('index2.html', status=500, res="Internal Server Error")
            
    return render_template('index2.html', status=500, res="Internal Server Error")


if __name__ == "__main__":
    app.run(debug=True)
