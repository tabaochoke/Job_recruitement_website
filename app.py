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
  job['id'] = row[0]
  job['title'] = row[1]
  job['location'] = row[2]
  job['salary'] = row[3]
  JOBS.append(job)
print(JOBS)


@app.route('/')
def hello_world():
  return render_template('home.html', JOBS=JOBS, company="Jovian")


@app.route('/api/jobs')
def return_jobs():
  return jsonify(cursor)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
