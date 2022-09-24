from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session, SessionTransaction


class SessionHandler:
    """
    Session class
    """

    def __init__(self, connection: Connection):
        """
        Constructor
        """
        self._session = Session(bind=connection)
        self._transaction: SessionTransaction = self._session.begin()

    def __del__(self):
        try:
            self._session.commit()
        except:
            self._transaction.rollback()
            raise
        finally:
            self._session.close()

    def get_session(self):
        """
        Returns the database session
        """
        return self._session
