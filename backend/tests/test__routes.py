import pytest
from application.app import app
import json


@pytest.fixture()
def client():
    app.config.update({
        "TESTING": True,
        'SQLALCHEMY_DATABASE_URI' : 'sqlite://'

    })
    with app.test_client() as client:
        yield client


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_coursecontent(client):
    response = client.get("api/coursecontent/1")
    assert response.status_code == 200
    assert response.json[0]['title'] == "Introduction"


def test_questions(client):
    response = client.get("/api/questions/1")
    assert response.status_code == 200
    assert response.json[0]['weeknumber'] == 1


def test_marks_all(client):
    response = client.get("/api/marks/all")
    assert response.status_code == 200

def test_marks_week(client):
    response = client.get("/api/marks/1")
    assert response.status_code == 200

def test_programming_assignement(client):
    response = client.get("/api/programmingassignments/1")
    assert response.status_code == 200
    assert response.json[0]['id'] == 1
    

def test_gasubmit(client):
    data = {
        "number":1,
        "weeknumber":1,
        "submitted_answers": ["A","B","C","D"]
    }
    data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    response = client.post("/api/gasubmit",headers = headers, data = data)
    assert response.status_code == 201
    assert response.json['weeknumber'] == 1

    data_fail = {
        "number":1000,
        "weeknumber":1000,
        "submitted_answers": ["A","B","C","D"]
    }
    data_fail = json.dumps(data_fail)
    response_fail = client.post("/api/gasubmit",headers = headers, data = data_fail)
    assert response_fail.status_code == 404


def test_programming_assignement_submission(client):
    data = {
    "weeknumber": 1,
    "assignment_id": 1,
    "user_output_public_test_case1": "0",
    "user_output_public_test_case2": "0",
    "user_output_public_test_case3": "0",
    "user_output_private_test_case1": "0",
    "user_output_private_test_case2": "0",
    "user_output_private_test_case3": "0"
    }
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)
    response = client.post("/api/pasubmit",headers = headers,data = data)

    assert response.status_code == 201

    data_fail = {
    "weeknumber": 1000,
    "assignment_id": 1000,
    "user_output_public_test_case1": "0",
    "user_output_public_test_case2": "0",
    "user_output_public_test_case3": "0",
    "user_output_private_test_case1": "0",
    "user_output_private_test_case2": "0",
    "user_output_private_test_case3": "0"
    }

    data_fail = json.dumps(data_fail)

    response_fail = client.post("/api/pasubmit",headers = headers,data = data_fail)
    assert response_fail.status_code == 404

def test_run_python(client):
    data = json.dumps({
    "code": "print(\"Hello World\")",
    "input_data": ""
    })
    headers = {'Content-Type': 'application/json'}

    response = client.post("/api/run-python",headers = headers,data = data)
    assert response.status_code == 200


def test_genAI_summary(client):
    response = client.get("/api/genai/summary/1/3")

    assert response.status_code == 200


def test_genAI_explaintheory(client):
    response = client.get("/api/genai/explaintheory/1")

    assert response.status_code == 200


def test_genAI_doubtbot(client):
    response = client.get("/api/genai/doubtbot/4")

    assert response.status_code == 200

def test_genAI_explainprogramming(client):
    response = client.get("/api/genai/explainprogramming/1")

    assert response.status_code == 200