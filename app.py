from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    "id": 1,
    "title": "Data Analyst",
    "location": "Sylhet, Bangladesh",
    "Salary": "BDT. 1000"
}, {
    "id": 2,
    "title": "Data Scientist",
    "location": "Dhaka, Bangladesh",
    "Salary": "BDT. 10,00,000"
}, {
    "id": 3,
    "title": "Data Engineer",
    "location": "Rajshahi, Bangladesh",
    "Salary": "BDT. 1,00,0000"
}, {
    "id": 4,
    "title": "Data Janwar",
    "location": "Khulna, Bangladesh",
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Tareq")


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
