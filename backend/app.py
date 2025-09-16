from flask import Flask, jsonify, request
from flask_cors import CORS
from recommender import recommend_for_job, get_jobs_meta

app = Flask(__name__)
CORS(app)

@app.route("/jobs", methods=["GET"])
def jobs():
    return jsonify(get_jobs_meta())

@app.route("/recommend/<int:job_id>", methods=["GET"])
def recommend(job_id):
    top_n = int(request.args.get("top_n", 10))
    try:
        results = recommend_for_job(job_id=job_id, top_n=top_n)
        return jsonify({"job_id": job_id, "top_n": top_n, "results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
