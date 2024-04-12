#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys

from sqlalchemy import create_engine, orm

from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(user, pwd, db_name)

    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = orm.Session(engine)

    new_state = State(name="Louisiana")

    session.add(new_state)

    session.commit()
    print("{}".format(new_state.id))
    session.close()
