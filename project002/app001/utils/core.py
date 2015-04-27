from app001.utils.settings import DB_SESSION


class Transaction(object):

    """For providing a transaction accross requests.
    The `with` `as` variable given is then used for sqlalchemy session calls,
    especially related to insert, update and delete operations.

    If an exception occurs all calls are rolled back.
    Otherwise everything is commited.

    """

    def __init__(self):
        """Constructor to setup the DB_SESSION object

        """
        self.session = DB_SESSION

    def __enter__(self):
        """Starts transaction by returning the DB_SESSION object

        """
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Rolls back transaction if an exception occurs.

        """
        if exc_type:
            err_msg = '\nRolled back due to:\n{exc_val}'.format(
                exc_val=exc_val)
            self.session.rollback()
        return True
