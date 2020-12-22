import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class EntityID(base):
    __abstract__ = True

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)