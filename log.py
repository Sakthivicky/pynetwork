from flask import Flask, request, jsonify
import logging

app = Flask(__name__)


logging.basicConfig(level=logging.INFO)

@app.before_request
def log_request_info():
    logging.info('Request Method: %s', request.method)
    logging.info('Request URL: %s', request.url)
    logging.info('Request Headers: %s', request.headers)
    logging.info('Request Body: %s', request.get_data(as_text=True))

@app.after_request
def log_response_info(response):
    logging.info('Response Status: %s', response.status)
    logging.info('Response Headers: %s', response.headers)
    logging.info('Response Body: %s', response.get_data(as_text=True))
    return response

@app.route('/example', methods=['POST'])
def example():
    data = request.get_json()
    return jsonify({"message": "Data received", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True)
