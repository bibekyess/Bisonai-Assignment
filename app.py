import json

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    list = []
    fileName = ['line.csv', 'bar_chart_D.csv', 'bar_chart_W.csv', 'bar_chart_M.csv']
    for i in range(len(fileName)):
        df = pd.read_csv(fileName[i])
        chart_data = df.to_dict(orient='records')
        chart_data = json.dumps(chart_data, indent=2)
        list.append({'chart_data': chart_data})
        
    return render_template("index.html", data=list[0], data1 = list[1], data2=list[2], data3 = list[3])

if __name__ == "__main__":
    app.run(debug=True)
