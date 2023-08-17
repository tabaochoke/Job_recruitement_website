from flask import Flask, render_template, jsonify, request
from database import  JOBS , insert_job

app = Flask(__name__)
@app.route('/' , methods=['GET', 'POST'])
def hello_world():
  
  return render_template('home.html', JOBS=JOBS, company="Jovian")


@app.route('/api/jobs')
def return_jobs():
  return jsonify(JOBS)


@app.route('/jobs/<id>' )
def return_job(id ):
  try:
    job_id = int(id)
    job = JOBS[job_id]
    
    return render_template('job_detail.html', job=job)
  except ValueError:
    return 'Invalid job ID'

@app.route('/jobs/<id>/process', methods=['POST'])
def process(id):
  first_name = request.form.get('First Name:')
  # process the data using Python code
  last_name = request.form.get('Last Name:')
  user_name = request.form.get('Username:')
  email = request.form.get('Email:')
  address = request.form.get('Address:')
  cv_url = request.form.get('CV URL:')
  country = request.form.get('Country:')
  state = request.form.get('State:')
  zip = request.form.get('Zip:')
  print  (first_name , last_name , user_name , email , address , cv_url , country , state , zip)
  insert_job (first_name, last_name, user_name, email, address, cv_url, country, state, zip)
  return render_template('job_detail.html', job=JOBS[int(id)])
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
