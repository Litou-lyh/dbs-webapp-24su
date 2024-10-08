######################################################################
# Copyright 2016, 2022 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
######################################################################

# spell: ignore Rofrano jsonify restx dbname
"""
Records Service with Swagger

Paths:
------
GET / - Displays a UI for Selenium testing
GET /records - Returns a list all of the Records
GET /records/{record_id} - Returns the Records with a given id number
POST /records - creates a new Records record in the database
PUT /records/{record_id} - updates a Records record in the database
DELETE /records/{record_id} - deletes a Records record in the database
"""

from flask import request, jsonify, url_for, abort
from flask import current_app as app  # Import Flask application
import pandas as pd
from service.models import Records
from service.common import status  # HTTP Status Codes
from service.ml_model import xgb, scaler


######################################################################
# GET HEALTH CHECK
######################################################################
@app.route("/health")
def healthcheck():
    """Let them know our heart is still beating"""
    return jsonify(status=200, message="Healthy"), status.HTTP_200_OK


######################################################################
# Configure the Root route before OpenAPI
######################################################################
@app.route("/")
def index():
    """Index page"""
    return app.send_static_file("index.html")


######################################################################
# LIST ALL RECORDS
######################################################################
@app.route("/records")
def list_records():
    """List all records"""
    app.logger.info("Request to list all records")
    records = Records.find_all()
    # print(records)
    results = [record.serialize() for record in records]
    return jsonify(results), status.HTTP_200_OK


######################################################################
# GET A RECORD
######################################################################
@app.route("/records/<int:record_id>", methods=["GET"])
def get_record(record_id):
    """Returns the Record with a given id number"""
    app.logger.info(f"Request for record with id: {record_id}")
    record = Records.query.get(record_id)

    if not record:
        abort(status.HTTP_404_NOT_FOUND, f"Record with id '{record_id}' was not found.")

    return jsonify(record.serialize()), status.HTTP_200_OK


######################################################################
# CREATE A RECORD
######################################################################
@app.route("/records", methods=["POST"])
def create_record():
    """Creates a new Record record in the database"""
    check_content_type("application/json")
    record_data = request.get_json()
    record = Records.deserialize(record_data)
    record.create()
    return (
        jsonify(record.serialize()),
        status.HTTP_201_CREATED,
        {"Location": url_for("get_record", record_id=record.id, _external=True)},
    )


######################################################################
# UPDATE A RECORD
######################################################################
@app.route("/records/<int:record_id>", methods=["PUT"])
def update_record(record_id):
    """Updates a Record record in the database"""
    check_content_type("application/json")
    record = Records.query.get(record_id)

    if not record:
        abort(status.HTTP_404_NOT_FOUND, f"Record with id '{record_id}' was not found.")

    record_data = request.get_json()
    record.update(record_data)
    return jsonify(record.serialize()), status.HTTP_200_OK


######################################################################
# DELETE A RECORD
######################################################################
@app.route("/records/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    """Deletes a Record based on the id specified in the path"""
    app.logger.info(f"Request to delete record with id: {record_id}")
    record = Records.query.get(record_id)

    if not record:
        abort(status.HTTP_404_NOT_FOUND, f"Record with id '{record_id}' was not found.")

    record.delete()
    return "", status.HTTP_204_NO_CONTENT


######################################################################
# PREDICT A RECORD
######################################################################
@app.route("/records/<int:record_id>/predict", methods=["GET"])
def predict_record(record_id):
    """Predict the cost of a health record with PUT request"""
    app.logger.info(f"Request to predict record with id: {record_id}")
    record = Records.query.get(record_id)

    if record:
        record = record.serialize()
    else:
        return "", status.HTTP_404_NOT_FOUND

    sex_cats = ["female", "male"]
    smoke_cats = ["no", "yes"]
    region_cats = ["southeast", "southwest", "northeast", "northwest"]

    record["smoke"] = smoke_cats[record["smoke"]]

    data = pd.DataFrame([record])

    data['sex'] = pd.Categorical(data['sex'], categories=sex_cats)
    data['smoke'] = pd.Categorical(data['smoke'], categories=smoke_cats)
    data['region'] = pd.Categorical(data['region'], categories=region_cats)

    data = pd.get_dummies(data, columns=["sex", "smoke", "region"])

    data["charges"] = 10000
    data[["age", "bmi", "children", "charges"]] = scaler.transform(data[["age", "bmi", "children", "charges"]])
    data = data.drop("charges", axis=1)

    columns = ['age', 'bmi', 'children', 'sex_female', 'sex_male', 'smoke_no', 'smoke_yes',
               'region_northeast', 'region_northwest', 'region_southeast', 'region_southwest']
    data = data[columns]
    prediction = xgb.predict(data)[0]
    result = {"cost": f"{prediction * scaler.scale_[-1] + scaler.mean_[-1]}"}

    return jsonify(result), status.HTTP_200_OK


######################################################################
# UTILITY FUNCTIONS
######################################################################
def check_content_type(content_type):
    """Checks that the media type is correct"""
    if "Content-Type" not in request.headers:
        app.logger.error("No Content-Type specified.")
        abort(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            "Content-Type must be application/json",
        )

    if request.headers["Content-Type"] != content_type:
        app.logger.error("Invalid Content-Type: %s", request.headers["Content-Type"])
        abort(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            "Content-Type must be application/json",
        )


######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################
