# DBS Project: End-to-end Insurance Cost Prediction Application

[![Build Status](https://github.com/Litou-lyh/dbs-webapp-24su/actions/workflows/tdd-tests.yml/badge.svg)](https://github.com/Litou-lyh/dbs-webapp-24su/actions)
[![Open in Remote - Containers](https://img.shields.io/static/v1?label=Remote%20-%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/Litou-lyh/dbs-webapp-24su)

The sample code is using [Flask micro-framework](http://flask.pocoo.org/). It also uses [PostgreSQL](https://www.postgresql.org) as a database. Input data will be passed through RestFUL API for backend processing. CRUD operations are implemented using Object–Relational Mapping (ORM), and data is then stored in PostgreSQL database. We integreated an XGBoost model for insurance cost prediction. The prediction function is also called by RestFUL API.

This repository is based on a lab from the *NYU DevOps and Agile Methodologies* graduate course [CSCI-GA.2820-001](https://cs.nyu.edu/courses/fall22/CSCI-GA.2820-001/) on Behavior Driven Development with Flask and Behave

## Introduction

Many enterprises still rely on structured data in traditional relational databases and data warehouses. However, to drive business growth, digital transformation, and enhance user experience and organizational excellence, they need real-time insights. To achieve this, enterprises are developing additional data sources to manage large amounts of unstructured data, enabling semi real-time big data analytics and the creation of machine/deep learning and AI digital solutions.

We try to build a project following this idea, and provide a end-to-end web app integrating relational database and ML models.

In this project, We focus on the business use case of insurance cost prediction: customer's health condition and daily habits are significant indicators to their insurance cost, and insurance companies rely heavily on precise prediction models to provide appropriate insurance policies and products. With machine learning models, for insurance companies, we help them accelerate cost assessment procedures, and lower their risks on unpredicted insurance claims; for customers, we help them get their suitable insurance products.

## What's featured in the project?

```text
./service/routes.py -- the main Service using Python Flask
./service/models.py -- the data models for persistence
./service/common -- a collection of status, error handlers and logging setup
./tests/test_routes.py -- unit test cases for the server
./tests/test_models.py -- unit test cases for the model
```


## Instruction of deployment and usage

### Deployment

#### Pull the Docker Image 

`docker pull gorgeous/dbs-webapp-24su:v6`

#### Run It Locally

`docker docker run --rm -p 8080:8080 --platform linux/amd64 gorgeous/dbs-webapp-24su:v6`

Now you can access in your browser with this URL: `http://localhost:8080/` 

### User guide
- To Create a health record:
  1. Fill out the form with valid data. (Leave Record ID blank; age must be positive integer; BMI must be positive number)
  2. Click "Create" button.
  3. Wait the record id appears in the form, together with a flash message says "success"

- To Retrieve a health record:
  1. Enter record id.
  2. Click "Retrieve" button.
  3. If succcess: all the fields will be filled with data, If fail: flash message says "404 Not Found"

- To Update a health record:
  1. Fill out the form with valid data, including Record ID of the record you want to modify.
  2. Click "Update" button.
  3. If success, then a flash message says "success". If you retrieve the record later, the fields will be updated.
 
- To Delete a health record:
  1. Enter record id.
  2. Click "Delete" button.
  3. If succcess: then a flash message says "Record has been Deleted!"; If the record does not exist: then a flash message says "Server error!"
 
- To predict the cost of a health record:
  1. After you create the record !!!
  2. Enter the record id.
  3. Click "Predict" button.
  4. If succcess: then a flash message says "Success" and the predicted results will be displayed in the result table below.
    - Cost: predicted insurance cost
    - Suggestion: suggestions to the insurance operator. (Accept, Conditional Accept, and Refuse)
    - Plan: different level of plans could be applied. (Normal, Enhanced Version, Extra Condition Version, and Only Endorsed by Manager)

---

 <div style="text-align: center; margin: 0 auto;">
  <img src="https://github.com/user-attachments/assets/e63d3da5-3f92-4515-9f19-aa02bba4bb1d" alt="homepage" width="75%">
  <p><strong>Figure 1: Homepage</strong></p>
</div>

<hr>

<div style="text-align: center; margin: 0 auto;">
  <img src="https://github.com/user-attachments/assets/a1d6aa56-c1d1-48d7-9373-b0aafeff093a" alt="create_record" width="75%">
  <p><strong>Figure 2: Create Record</strong></p>
</div>

<hr>

<div style="text-align: center; margin: 0 auto;">
  <img src="https://github.com/user-attachments/assets/85780f79-56bb-4f07-8845-6a496db00bf6" alt="example_of_invalid_data" width="75%">
  <p><strong>Figure 3: Example of Invalid Data</strong></p>
</div>

<hr>

<div style="text-align: center; margin: 0 auto;">
  <img src="https://github.com/user-attachments/assets/a2b4e045-3123-4493-af57-c36f732cebfc" alt="prediction" width="75%">
  <p><strong>Figure 4: Prediction</strong></p>
</div>

<hr>

<div style="text-align: center; margin: 0 auto;">
  <img src="https://github.com/user-attachments/assets/ebef20b1-250a-4fc8-8640-19369a37cf52" alt="example_of_refuse" width="75%">
  <p><strong>Figure 5: Example of Refuse</strong></p>
</div>


 
## License

Copyright (c) 2016, 2024, John J. Rofrano. All rights reserved.

Licensed under the Apache License. See [LICENSE](LICENSE)

This repository is part of the NYU graduate class **CSCI-GA.2810-001: DevOps and Agile Methodologies** taught by [John Rofrano](http://cs.nyu.edu/~rofrano/), Adjunct Instructor, NYU Courant Institute, Graduate Division, Computer Science.
