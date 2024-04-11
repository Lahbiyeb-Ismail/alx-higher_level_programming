#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine, orm)

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db_link = 'mysql+mysqldb://{}:\
              {}@localhost/{}'.format(user, password, db_name)

    engine = create_engine(db_link, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = orm.Session(engine)

    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
