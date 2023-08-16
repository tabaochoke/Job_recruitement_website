from flask import Flask, render_template, jsonify
from database import cursor

app = Flask(__name__)

# JOBS = [
#   {
#     'id' : 1,
#     'title' : 'Data Analyst',
#     'location': 'Bengaluru , India',
#     'salary' : 'Rs. 15,00,000'
#   },
#   {
#     'id' : 2,
#     'title' : 'Data Scientist',
#     'location': 'Delhi , India',
#     'salary' : 'Rs. 15,00,000'
#   },
#   {
#     'id' : 3,
#     'title' : 'Frontend Engineer',
#     'location': 'Remote',
#   },
#   {
#     'id' : 4,
#     'title' : 'Backend Engineer',
#     'location': 'San Francisco',
#     'salary' : '$120000'
#   }
# ]
JOBS = []
for row in cursor:
  job = {}
  job['id'] = int(row[0]) - 1
  job['title'] = row[1]
  job['location'] = row[2]
  job['salary'] = row[3]
  job['repon'] = row[5]
  job['require'] = row[6]
  job['create'] = row[7]
  job['update'] = row[8]
  JOBS.append(job)


@app.route('/')
def hello_world():
  return render_template('home.html', JOBS=JOBS, company="Jovian")


@app.route('/api/jobs')
def return_jobs():
  return jsonify(JOBS)


@app.route('/jobs/<id>')
def return_job(id):
  try:
    job_id = int(id)
    job = JOBS[job_id]
    return render_template('job_detail.html', job=job)
  except ValueError:
    return 'Invalid job ID'
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
