from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for the latest sensor data
latest_data = {
    "voltage": 5.8,
    "current": 1.2,
    "tempLeft": 34.0,
    "tempRight": 35.0,
    "ldrLeft": 85.0,
    "ldrRight": 82.0
}

@app.route('/')
def index():
    # Serves the HTML dashboard
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    # Frontend calls this to get the latest data
    return jsonify(latest_data)

@app.route('/api/update', methods=['POST'])
def update_data():
    # Your ESP8266 will send data here
    global latest_data
    data = request.json
    if data:
        latest_data.update(data)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)