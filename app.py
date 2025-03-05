import psutil
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    message = None

    if cpu_metric > 80 or mem_metric > 80:
        message = "⚠️ High CPU or Memory Detected, scale up!!!"

    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=message)

# New API route for real-time metrics
@app.route("/metrics")
def metrics():
    return jsonify({
        "cpu_metric": psutil.cpu_percent(),
        "mem_metric": psutil.virtual_memory().percent
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
