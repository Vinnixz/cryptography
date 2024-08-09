from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Table = declarative_base()


class User(Table):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    document = Column(String(255))
    credit_card = Column(String(255))

    @staticmethod
    def migrate(engine):
        Table.metadata.create_all(engine)
