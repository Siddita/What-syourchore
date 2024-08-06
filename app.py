from flask import Flask, render_template, jsonify

app = Flask(__name__)

job_list = [
    {"id": 1, "title": "Software Engineer", "location": "San Francisco, CA", "salary": "$120,000"},
    {"id": 2, "title": "Data Scientist", "location": "New York, NY", "salary": "$115,000"},
    {"id": 3, "title": "Web Developer", "location": "Austin, TX", "salary": "$90,000"},
]

@app.route("/")
def home():
    return render_template('home.html', jobs=job_list)

@app.route("/jobs")
def list_jobs():
    return jsonify(job_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
