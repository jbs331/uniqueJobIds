from flask import Flask, jsonify, make_response
from uuid import uuid4
import random
import time

app = Flask(__name__)

@app.route('/getjobdetails/<job_id>')
def getJobDetails(job_id):
    # Simulate delay 10% of the time
    if random.random() < 0.1:  # 10% chance to simulate delay
        time.sleep(random.randint(1, 10))  # Random delay between 1 and 10 seconds

    # Simulate a network error with a 10% probability
    if random.random() < 0.1:  # 10% chance to simulate network error
        return make_response(jsonify(error="Network error occurred"), 500)

    # Return a JSON response with a UUID
    response = jsonify(jobId=str(uuid4()))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
