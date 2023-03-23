import sys
from flask import render_template, redirect, url_for, request, abort

from models.User import User

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def index():
    return "index"


def store():
    return "store"


def show(userId):
    return "show"


def update(userId):
    return "update"


def delete(userId):
    return "delete"
