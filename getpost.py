from flask import Flask, request, jsonify

app = Flask(__name__)

# GET endpoint example
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "message": "GET request successful",
        "data": {"user": "Tanvir", "role": "MLOps Engineer"}
    })

# POST endpoint example 
@app.route('/api/contact', methods=['POST'])
def post_contact():
    data = request.json
    print(f"Received contact submission: {data}")
    return jsonify({
        "status": "Message received",
        "email": data.get('email'),
        "message": data.get('message')
    })

if __name__ == '__main__':
    app.run(port=5000)