#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine, orm)

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pwd, db_name)

    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = orm.Session(engine)
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
