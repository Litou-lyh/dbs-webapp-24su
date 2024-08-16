# Copyright 2016, 2024 John Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Models for Records Demo Service

All of the models are stored in this module

Models
------
Records

Attributes:
-----------
id
first_name
last_name
age
sex
bmi
children
smoke
region

"""
import logging
from flask_sqlalchemy import SQLAlchemy

logger = logging.getLogger("flask.app")

# Create the SQLAlchemy object to be initialized later in init_db()
db = SQLAlchemy()


class DataValidationError(Exception):
    """Used for an data validation errors when deserializing"""


class Records(db.Model):
    """
    Class that represents a Record in the dataset.
    """

    ##################################################
    # Table Schema
    ##################################################
    id = db.Column(db.Integer, primary_key=True)  # pylint: disable=invalid-name
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)  # 'Male' or 'Female'
    bmi = db.Column(db.Float, nullable=False)
    children = db.Column(db.Integer, nullable=False)
    smoke = db.Column(db.Boolean, nullable=False)
    region = db.Column(db.String(100), nullable=False)

    ##################################################
    # Methods
    ##################################################

    def serialize(self):
        """Returns the object data in easily serializable format"""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "sex": self.sex,
            "bmi": self.bmi,
            "children": self.children,
            "smoke": self.smoke,
            "region": self.region,
        }

    @classmethod
    def deserialize(cls, data):
        """Deserializes Records from a dictionary."""
        try:
            return cls(
                first_name=data["first_name"],
                last_name=data["last_name"],
                age=data["age"],
                bmi=data["bmi"],
                sex=data["sex"],
                children=data["children"],
                smoke=data["smoke"],
                region=data["region"],
            )
        except KeyError as e:
            raise DataValidationError("Invalid record: missing " + e.args[0]) from e

    def create(self):
        """Adds a new Record to the database."""
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """Updates a Record with data from a dictionary."""
        for key, value in data.items():
            setattr(self, key.lower().replace(" ", "_"), value)
        db.session.commit()

    def delete(self):
        """Deletes a Record from the database."""
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        """Returns all Records."""
        return cls.query.all()
