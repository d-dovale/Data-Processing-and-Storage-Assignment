class InMemoryDB:
    def __init__(self):
        """
        Initialize the in-memory database with an empty main database and no active transaction.
        """
        self.main_db = {}
        self.transaction_db = None
        self.in_transaction = False

    def begin_transaction(self):
        """
        Starts a new transaction.
        Raises an exception if a transaction is already in progress.
        """
        if self.in_transaction:
            raise Exception("Transaction already in progress.")
        self.transaction_db = {}
        self.in_transaction = True

    def put(self, key, value):
        """
        Adds or updates a key-value pair within an active transaction.
        Raises an exception if no transaction is in progress.
        """
        if not self.in_transaction:
            raise Exception("No active transaction.")
        self.transaction_db[key] = value

    def get(self, key):
        """
        Retrieves the value associated with a key from the main database.
        Returns None if the key does not exist.
        """
        return self.main_db.get(key, None)

    def commit(self):
        """
        Commits all changes made during the transaction to the main database.
        Raises an exception if no transaction is in progress.
        """
        if not self.in_transaction:
            raise Exception("No active transaction to commit.")
        self.main_db.update(self.transaction_db)
        self.transaction_db = None
        self.in_transaction = False

    def rollback(self):
        """
        Aborts all changes made during the transaction.
        Raises an exception if no transaction is in progress.
        """
        if not self.in_transaction:
            raise Exception("No active transaction to rollback.")
        self.transaction_db = None
        self.in_transaction = False

# Sample usage and testing
if __name__ == "__main__":
    db = InMemoryDB()

    # Should return None, because "A" doesn't exist
    print('db.get("A"):', db.get("A"))

    # Should raise an error because no transaction is in progress
    try:
        db.put("A", 5)
    except Exception as e:
        print("Error:", e)

    # Start a new transaction
    db.begin_transaction()

    # Set "A" to 5 within the transaction
    db.put("A", 5)

    # Should still return None, because "A" is not committed yet
    print('db.get("A") after put in transaction:', db.get("A"))

    # Update "A" to 6 within the transaction
    db.put("A", 6)

    # Commit the transaction
    db.commit()

    # Now "A" should return 6
    print('db.get("A") after commit:', db.get("A"))

    # Should raise an error because there is no active transaction
    try:
        db.commit()
    except Exception as e:
        print("Error:", e)

    # Should raise an error because there is no active transaction
    try:
        db.rollback()
    except Exception as e:
        print("Error:", e)

    # Should return None because "B" doesn't exist
    print('db.get("B"):', db.get("B"))

    # Start a new transaction
    db.begin_transaction()

    # Set "B" to 10 within the transaction
    db.put("B", 10)

    # Rollback the transaction
    db.rollback()

    # "B" should still be None
    print('db.get("B") after rollback:', db.get("B"))
