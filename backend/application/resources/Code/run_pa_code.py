from flask import request, jsonify
from flask_restful import Resource
import subprocess
import tempfile

class RunProgAssign(Resource):
    def post(self):
        data = request.get_json()
        
        # Getting code and input
        code = data.get('code')
        input_data = data.get('input', '')

        # print(f"Received code: {code}")
        # print(f"Received input_data: {input_data} (type: {type(input_data)})")

        # Checking if if input data is not a dict
        if isinstance(code, dict):
            return jsonify({'error': 'Code must be a string.'}), 400
        
        if not isinstance(input_data, str):
            input_data = str(input_data)

        try:
            with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as temp_file:
                temp_file.write(code.encode())
                temp_file.flush()
                result = subprocess.run(['python', temp_file.name], input=input_data, capture_output=True, text=True)
                output = result.stdout + result.stderr
        except Exception as e:
            output = str(e)

        return jsonify({'output': output})