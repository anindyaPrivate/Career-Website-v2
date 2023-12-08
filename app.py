from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS= [
  {
     "id": 1, 
     "title": "Software Developer", 
     "location": "Kolkata,India", 
     "salary": "Rs.18,00,000"
  },
  {
     "id": 2, 
     "title": "Data Engineer", 
     "location": "Hydrabad,India", 
     "salary": "Rs.16,00,000"
  },
  {
     "id": 3, 
     "title": "Frontend Developer", 
     "location": "Delhi,India" 
    
  },
  {
     "id": 4, 
     "title": "Backend Developer", 
     "location": "Remote", 
     "salary": "$80,000"
  }
]

@app.route("/")
def hello_Jovian():
  return render_template('home.html',
                        jobs = JOBS)

@app.route("/api/jobs") 
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

