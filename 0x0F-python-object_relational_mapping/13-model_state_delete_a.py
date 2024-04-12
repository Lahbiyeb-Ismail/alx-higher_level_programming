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

    db_link = 'mysql+mysqldb://{}:\
              {}@localhost/{}'.format(user, password, db_name)

    engine = create_engine(db_link, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = orm.Session(engine)

    session.query(State).delete(State.name.like("%a%"))

    session.commit()

    session.close()
