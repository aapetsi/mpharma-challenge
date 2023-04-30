from dotenv import load_dotenv

load_dotenv()

import pytest
from app import app
import json
from io import BytesIO


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def create_record(client):
    # create record
    record_to_create = {
        "category_code": "A00",
        "diagnosis_code": "A000",
        "full_code": "A00.0",
        "abbreviated_description":
        "Cholera due to Vibrio cholerae 01, biovar cholerae",
        "full_description":
        "Cholera due to Vibrio cholerae 01, biovar cholerae",
        "category_title": "Cholera"
    }
    response = client.post('/codes', json=record_to_create)
    assert response.status_code == 200
    new_record_id = json.loads(response.data)['id']
    return new_record_id


def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == "Server is running 🚀"


def test_index(client):
    response = client.get('/codes')
    assert response.status_code == 200


def test_get(client):
    # create a new record
    new_record_id = create_record(client)

    # retrieve the newly created record using its ID
    response = client.get(f'/codes/{new_record_id}')
    assert response.status_code == 200
    assert json.loads(response.data)['id'] == new_record_id


def test_get_not_found(client):
    response = client.get('/codes/999')
    assert response.status_code == 404
    assert json.loads(response.data)['message'] == 'Record not found'


def test_delete(client):
    new_record_id = create_record(client)
    response = client.delete(f'/codes/{new_record_id}')
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'Record deleted'


def test_delete_not_found(client):
    response = client.delete('/codes/999')
    assert response.status_code == 404
    assert json.loads(response.data)['message'] == 'Record not found'


def test_update(client):
    new_record_id = create_record(client)
    data = {
        "category_code": "A1",
        "diagnosis_code": "B2",
        "full_code": "C3",
        "abbreviated_description": "updated description",
        "full_description": "updated description",
        "category_title": "updated category"
    }
    response = client.put(f'/codes/{new_record_id}', json=data)
    assert response.status_code == 200
    assert json.loads(
        response.data
    )['abbreviated_description'] == data['abbreviated_description']


def test_update_not_found(client):
    data = {
        "category_code": "A1",
        "diagnosis_code": "B2",
        "full_code": "C3",
        "abbreviated_description": "updated description",
        "full_description": "updated description",
        "category_title": "updated category"
    }
    response = client.put('/codes/999', json=data)
    assert response.status_code == 404
    assert json.loads(response.data)['message'] == 'Record not found'


def test_create(client):
    data = {
        "category_code": "A1",
        "diagnosis_code": "B2",
        "full_code": "C3",
        "abbreviated_description": "new description",
        "full_description": "new description",
        "category_title": "new category"
    }
    response = client.post('/codes', json=data)
    assert response.status_code == 200
    assert json.loads(
        response.data
    )['abbreviated_description'] == data['abbreviated_description']


def test_upload(client):
    # Create a temporary file for testing
    csv_data = 'category_code,diagnosis_code,full_code,abbreviated_description,full_description,category_title\nA0,1234,A01234,Comma-ind anal ret,Comma-induced anal retention,Malignant neoplasm of anus and anal canal\n'
    csv_file = BytesIO(csv_data.encode('utf-8'))
    csv_file.name = 'sample_upload.csv'

    # Send a POST request to the endpoint with the test CSV file
    response = client.post('/upload',
                           data=dict(sample_upload=csv_file),
                           content_type='multipart/form-data')

    # Check the response status code
    assert response.status_code == 201

    # Check the response data
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['category_code'] == 'A0'
    assert data[0]['diagnosis_code'] == '1234'
    assert data[0]['full_code'] == 'A01234'
    assert data[0]['abbreviated_description'] == 'Comma-ind anal ret'
    assert data[0]['full_description'] == 'Comma-induced anal retention'
    assert data[0][
        'category_title'] == 'Malignant neoplasm of anus and anal canal'
