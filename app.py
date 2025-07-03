from flask import Flask, request, jsonify
from lead_generation.crew import LeadGeneration
import json
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/run/init', methods=['POST'])
def run_initial():
    try:
        data = request.get_json()
        topic = data.get("topic", "")

        inputs = {
            'topic': topic,
            "developer_skills": {
                "skill": ["HTML", "CSS", "JavaScript", "Laravel"]
            }
        }

        output = LeadGeneration().classifier_crew().kickoff(inputs=inputs)
        output_text = str(output).strip()

        return jsonify({
            "status": "success",
            "type": output_text
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/run/checkpoints', methods=['POST'])
def run_with_checkpoints():
    try:
        data = request.get_json()
        topic = data.get("topic", "")
        checkpoints = data.get("checkpoints", [])

        inputs = {
            'topic': topic,
            'checkpoints': checkpoints,
            "developer_skills": {
                "skill": ["HTML", "CSS", "JavaScript", "Laravel"]
            }
        }

        result = LeadGeneration().project_crew().kickoff(inputs=inputs)

        raw_output = result.raw.strip() if hasattr(result, 'raw') else str(result)
        cleaned = re.sub(r"^(`{3,}\s*)?(json)?", "", raw_output.strip(), flags=re.IGNORECASE)
        cleaned = re.sub(r"`{3,}$", "", cleaned).strip()

        try:
            parsed_result = json.loads(cleaned)
        except json.JSONDecodeError:
            parsed_result = {"message": cleaned}

        return jsonify({
            "status": "success",
            "result": parsed_result
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/run/job', methods=['POST'])
def run_job():
    try:
        data = request.get_json()
        topic = data.get("topic", "")
        checkpoints = data.get("checkpoints", [])  # ✅ FIXED: define checkpoints

        inputs = {
            'topic': topic,
            'checkpoints': checkpoints,
            "developer_skills": {
                "skill": ["HTML", "CSS", "JavaScript", "Laravel"]
            }
        }

        result = LeadGeneration().job_crew().kickoff(inputs=inputs)

        raw_output = result.raw.strip() if hasattr(result, 'raw') else str(result)
        cleaned = re.sub(r"^(`{3,}\s*)?(json)?", "", raw_output.strip(), flags=re.IGNORECASE)
        cleaned = re.sub(r"`{3,}$", "", cleaned).strip()

        try:
            parsed_result = json.loads(cleaned)
        except json.JSONDecodeError:
            parsed_result = {"message": cleaned}

        return jsonify({
            "status": "success",
            "result": parsed_result
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)