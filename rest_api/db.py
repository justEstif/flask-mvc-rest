from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)


@contextmanager
def transaction():
    try:
        yield
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise


def persist(*args):
    db.session.add_all(args)


def delete(obj):
    db.session.delete(obj)


def execute(sql):
    return db.session.execute(sql)
