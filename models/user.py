#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """ Representation of a user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
