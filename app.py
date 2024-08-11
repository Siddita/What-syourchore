from flask import Flask, render_template, jsonify
from database import load_jobs_from_db


app = Flask(__name__)



@app.route("/")
def home():
    job = load_jobs_from_db()  
    return render_template('home.html', jobs=job, company_name='whatsthechore')


@app.route("/jobs")
def list_jobs():
    job_list = load_jobs_from_db() 
    return jsonify(job_list)  


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
