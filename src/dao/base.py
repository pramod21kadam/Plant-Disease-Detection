from datamodel.master import db
from packages.packages import exc, func
class base:
    def insert(obj):
        """
            Add data into Database.\n
            Returns true for successful insertion
        """
        try:
            db.session.add(obj)
            return True
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            print(f"Insert error:- {e}")
            return False
        except Exception as e:
            print(f"Insert error:- {e}")
            return False
    
    def delete(obj):
        """
            Delete data from database.\n
            Returns true for successful deletion
        """
        try:
            db.session.delete(obj)
            return True
        except exc.IntegrityError as e:
            db.session.rollback()
            print(f"Commit error(1):- {e}")
            return False
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            print(f"Commit error(2):- {e}")
            return False
        except Exception as e:
            print(e)
            return False

    def commit():
        """
            Commit to database.\n
            Returns true on successful commit
        """
        try:
            db.session.commit()
            return True
        except exc.IntegrityError as e:
            db.session.rollback()
            print(f"Commit error(1):- {e}")
            return False
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            print(f"Commit error(2):- {e}")
            return False
        except Exception as e:
            print(e)
            return False