import os

from flask import current_app

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# Import types for using them from single entrypoint bd.py
from sqlalchemy import Column, String, Integer, Boolean


def get_db_uri():
    _db_uri = os.environ.get('DATABASE_URI')
    msg = 'Get DATABASE_URI from environ'

    if not _db_uri:
        _db_uri = current_app.config.get('DATABASE_URI')
        msg = 'Get DATABASE_URI from app.config'

    current_app.logger.info(msg)

    if not _db_uri:
        raise Exception(
            'DATABASE_URI must be set in app.config or Environment variable')

    return _db_uri


engine = create_engine(get_db_uri())
db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
))
Base = declarative_base()
Base.query = db_session.query_property()


def shutdown_session(exception=None):
    db_session.remove()


def init_app(app):
    """Removes db session when app is closing"""
    app.teardown_appcontext(shutdown_session)


def init_db():
    """Create database and all loaded tables provided by ORM"""
    Base.metadata.create_all(bind=engine)


def drop_db(only_orm=True):
    """Drop all tables in database

    Tables that exists in DB, but not in metadata
    will be dropped either
    """
    if not only_orm:
        Base.metadata.reflect(bind=engine)
    Base.metadata.drop_all(bind=engine)
