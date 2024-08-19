# DBS Project: End-to-end Insurance Cost Prediction Application

[![Build Status](https://github.com/Litou-lyh/dbs-webapp-24su/actions/workflows/tdd-tests.yml/badge.svg)](https://github.com/Litou-lyh/dbs-webapp-24su/actions)
[![Open in Remote - Containers](https://img.shields.io/static/v1?label=Remote%20-%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/Litou-lyh/dbs-webapp-24su)

The sample code is using [Flask micro-framework](http://flask.pocoo.org/). It also uses [PostgreSQL](https://www.postgresql.org) as a database. Input data will be passed through RestFUL API for backend processing. CRUD operations are implemented using Object–Relational Mapping (ORM), and data is then stored in PostgreSQL database. We integreated an XGBoost model for insurance cost prediction. The prediction function is also called by RestFUL API.

This repository is based on a lab from the *NYU DevOps and Agile Methodologies* graduate course [CSCI-GA.2820-001](https://cs.nyu.edu/courses/fall22/CSCI-GA.2820-001/) on Behavior Driven Development with Flask and Behave

## Introduction

Many enterprises still rely on structured data in traditional relational databases and data warehouses. However, to drive business growth, digital transformation, and enhance user experience and organizational excellence, they need real-time insights. To achieve this, enterprises are developing additional data sources to manage large amounts of unstructured data, enabling semi real-time big data analytics and the creation of machine/deep learning and AI digital solutions.

We try to build a project following this idea, and provide a end-to-end web app integrating relational database and ML models.

In this project, We focus on the business use case of insurance cost prediction: customer's health condition and daily habits are significant indicators to their insurance cost, and insurance companies rely heavily on precise on prediction models to provide appropriate insurance policies and products. With machine learning models, for insurance companies, we help them accelerate cost assessment procedures, and lower their risks on unpredicted insurance claims; for customers, we help them get their suitable insurance products.

## What's featured in the project?

```text
./service/routes.py -- the main Service using Python Flask
./service/models.py -- the data models for persistence
./service/common -- a collection of status, error handlers and logging setup
./tests/test_routes.py -- unit test cases for the server
./tests/test_models.py -- unit test cases for the model
```

## License

Copyright (c) 2016, 2024, John J. Rofrano. All rights reserved.

Licensed under the Apache License. See [LICENSE](LICENSE)

This repository is part of the NYU graduate class **CSCI-GA.2810-001: DevOps and Agile Methodologies** taught by [John Rofrano](http://cs.nyu.edu/~rofrano/), Adjunct Instructor, NYU Courant Institute, Graduate Division, Computer Science.
