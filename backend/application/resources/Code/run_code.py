from flask import request, jsonify
from flask_restful import Resource
import subprocess
import tempfile

class RunPython(Resource):
    def post(self):
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