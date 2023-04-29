import psycopg2
from flask import Flask, jsonify, request
import csv
import os
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)

conn = psycopg2.connect(host='localhost',
                        database='mpharma-dev',
                        user='apetsiampiah')


class DiagnosisCode:

    def to_dict(row):
        return {
            'id': row[0],
            'category_code': row[1],
            'diagnosis_code': row[2],
            'full_code': row[3],
            'abbreviated_description': row[4],
            'full_description': row[5],
            'category_title': row[6]
        }


@app.route('/')
def hello():
    return jsonify({'message': "Server is running 🚀"})


@app.route('/codes')
def index():
    page = request.args.to_dict().get('page', 1)
    offset = 20 * (int(page) - 1)
    cur = conn.cursor()
    cur.execute("SELECT * FROM diagnosis_codes LIMIT 20 OFFSET %s", (offset, ))
    codes = cur.fetchall()
    res = []
    for row in codes:
        res.append(DiagnosisCode.to_dict(row))

    return jsonify(res), 200


@app.route('/codes/<int:code_id>')
def get(code_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM diagnosis_codes WHERE id = %s", (code_id, ))
    code = cur.fetchone()

    if code is None:
        return jsonify({'message': 'Record not found'}), 404

    return jsonify(DiagnosisCode.to_dict(code))


@app.route('/codes/<int:code_id>', methods=["DELETE"])
def delete(code_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM diagnosis_codes WHERE id = %s", (code_id, ))

    if cur.rowcount == 0:
        return jsonify({'message': 'Record not found'}), 404

    conn.commit()

    return jsonify({'message': 'Record deleted'}), 200


@app.route('/codes/<int:code_id>', methods=["PUT"])
def update(code_id):
    data = request.get_json()
    cur = conn.cursor()
    cur.execute("SELECT * FROM diagnosis_codes WHERE id = %s", (code_id, ))
    row = cur.fetchone()

    if row is None:
        return jsonify({'message': 'Record not found'}), '404'
    record_to_update = (data["category_code"], data["diagnosis_code"],
                        data["full_code"], data["abbreviated_description"],
                        data["full_description"], data["category_title"],
                        code_id)
    cur.execute(
        "UPDATE diagnosis_codes SET category_code=%s, diagnosis_code=%s, full_code=%s, abbreviated_description=%s, full_description=%s, category_title=%s where id = %s returning *",
        record_to_update)
    updated_record = cur.fetchone()
    conn.commit()
    return jsonify(DiagnosisCode.to_dict(updated_record))


@app.route('/codes', methods=['POST'])
def create():
    cur = conn.cursor()
    data = request.get_json()
    record_to_insert = (data['category_code'], data['diagnosis_code'],
                        data['full_code'], data['abbreviated_description'],
                        data['full_description'], data['category_title'])
    cur.execute(
        "INSERT INTO diagnosis_codes (category_code, diagnosis_code, full_code, abbreviated_description, full_description, category_title) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *",
        record_to_insert)
    code = cur.fetchone()

    conn.commit()

    return jsonify(DiagnosisCode.to_dict(code))


@app.route('/upload', methods=["POST"])
def upload():
    cur = conn.cursor()
    csv_file = request.files.get('sample_upload')

    # Check if the file is empty
    if csv_file.seek(0, os.SEEK_END) == 0:
        return jsonify({'message': 'Empty file'})

    csv_file.seek(0)
    df = pd.read_csv(csv_file)

    new_data = []

    for _, row in df.iterrows():
        record_to_insert = (row['category_code'], row['diagnosis_code'],
                            row['full_code'], row['abbreviated_description'],
                            row['full_description'], row['category_title'])
        cur.execute(
            "INSERT INTO diagnosis_codes (category_code, diagnosis_code, full_code, abbreviated_description, full_description, category_title) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *",
            record_to_insert)
        r = cur.fetchone()
        conn.commit()
        new_data.append(DiagnosisCode.to_dict(r))

    return jsonify(new_data)
