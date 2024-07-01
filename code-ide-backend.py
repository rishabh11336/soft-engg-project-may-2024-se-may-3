from flask import Flask, request, jsonify
import subprocess
import tempfile
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/run-python', methods=['POST'])
def run_python():
    data = request.get_json()
    code = data['code']
    try:
        with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as temp_file:
            temp_file.write(code.encode())
            temp_file.flush()
            result = subprocess.run(['python', temp_file.name], capture_output=True, text=True)
            output = result.stdout + result.stderr
    except Exception as e:
        output = str(e)
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
