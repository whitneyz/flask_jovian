#print('hello world')

from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data analyst',
  'location': 'San Francisco, USA',
  'salary': '$120.000'
}, {
  'id': 2,
  'title': 'Data scientist',
  'location': 'Amsterdam, NL',
  'salary': '€70.000'
}, {
  'id': 3,
  'title': 'Frontend engineer',
  'location': 'Brussels, BE',
  'salary': '€50.000'
}, {
  'id': 4,
  'title': 'Backend engineer',
  'location': 'remote',
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__': app.run(host='0.0.0.0', debug=True)
