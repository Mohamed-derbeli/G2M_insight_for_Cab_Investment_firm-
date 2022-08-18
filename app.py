import numpy as np
import pickle5
from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle5.load(open('models/RFRegressor.pkl', 'rb'))

@app.route('/')
def index():
    return render_template(
        'index.html',
        data1=[{'GeN': 'Gender'}, {'GeN': 0}, {'GeN': 1}],
        data2=[{'MN': 'Month'}, {'MN': 1}, {'MN': 2}, {'MN': 3}, {'MN': 4}, {'MN': 5}, {'MN': 6}, {'MN': 7}, {'MN': 8},
               {'MN': 9}, {'MN': 10}, {'MN': 11}, {'MN': 12}],
        data3=[{'CO': 'Company'}, {'CO': 0}, {'CO': 1}],
        data4=[{'CY': 'City'}, {'CY': 1}, {'CY': 2}, {'CY': 3}, {'CY': 4}, {'CY': 5}, {'CY': 6}, {'CY': 7}, {'CY': 8},
               {'CY': 9}, {'CY': 10}, {'CY': 11}, {'CY': 12}, {'CY': 13}, {'CY': 14}, {'CY': 15}, {'CY': 16},
               {'CY': 17}, {'CY': 18}])


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    input_data = list(request.form.values())
    if int(input_data[0]) & int(input_data[1]) & input_data[2].isdigit() & input_data[3].isdigit() & input_data[4].isdigit()& input_data[4].isdigit()== True:
        pass
    else:
        print(ValueError)

    input_values = [x for x in input_data]
    arr_val = [np.array(input_values)]
    prediction = model.predict(arr_val)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=" The price of the transaction will be around: {}".format(output),
                           data1=[{'GeN': 'Gender'}, {'GeN': 0}, {'GeN': 1}],
                           data2=[{'MN': 'Month'}, {'MN': 1}, {'MN': 2}, {'MN': 3}, {'MN': 4}, {'MN': 5}, {'MN': 6}, {'MN': 7}, {'MN': 8}, {'MN': 9}, {'MN': 10}, {'MN': 11}, {'MN': 12}],
                           data3=[{'CO': 'Company'}, {'CO': 0}, {'CO': 1}],
                           data4=[{'CY': 'City'}, {'CY': 1}, {'CY': 2}, {'CY': 3}, {'CY': 4}, {'CY': 5}, {'CY': 6}, {'CY': 7}, {'CY': 8}, {'CY': 9}, {'CY': 10},{'CY': 11}, {'CY': 12}, {'CY': 13}, {'CY': 14}, {'CY': 15},{'CY': 16}, {'CY': 17}, {'CY': 18}])


if __name__ == '__main__':
    app.run(debug=True)
