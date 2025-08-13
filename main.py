# venv/main.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, jsonify
from utils.database import Database
from Repository.job import Job
from Repository.candidate import Candidate
from Repository.application import Application  # Import Application class

app = Flask(__name__)

# Create instances of the models
with Database() as db:
    job_model = Job(db)
    candidate_model = Candidate(db)
    application_model = Application(db)  # Instantiate Application model

# Writing endpoints
@app.route('/available_jobs', methods=['GET'])
def get_available_jobs():
    available_jobs = job_model.get_available_jobs()
    return jsonify({'jobs': available_jobs})

@app.route('/add_job', methods=['POST'])
def add_job():
    data = request.json
    job_id = job_model.add_job(data['skills'], data['requirements'], data['position'], data['location'])
    return jsonify({'job_id': job_id}), 201

@app.route('/add_candidate', methods=['POST'])
def add_candidate():
    data = request.json
    candidate_id = candidate_model.add_candidate(data['name'], data['major'], data['previous_job'], data['years_of_experience'])
    return jsonify({'candidate_id': candidate_id}), 201

@app.route('/all_candidates', methods=['GET'])
def get_all_candidates():
    all_candidates = candidate_model.get_all_candidates()
    return jsonify({'candidates': all_candidates})

@app.route('/add_application', methods=['POST'])
def add_application():
    data = request.json
    candidate_id = data['candidate_id']
    job_id = data['job_id']
    status = data['status']
    application_id = application_model.add_application(candidate_id, job_id, status)
    return jsonify({'application_id': application_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
