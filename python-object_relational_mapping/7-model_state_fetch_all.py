#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Création du moteur de connexion SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session pour communiquer avec la base
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer tous les objets State triés par id
    states = session.query(State).order_by(State.id.asc()).all()

    # Affichage des résultats au format "id: name"
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Fermeture de la session
    session.close()
