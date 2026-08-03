import pytest
from db.db import Database

@pytest.fixture
def db():
    """provides a fresh instance of the Database class ad cleans up after the test"""
    databse = Database()
    yield databse # provide the fixture instance , yileds the db when its used and then does the clean below ⬇️ 
    # - anything before or at yield runs before the test kind of like a setup operation anything after yield will run as a teardown step or clean up step after every test
    databse.data.clear() # Cleanup step (not needed for in-memory, but useful for real DBs)
    
    def test_add_user(db):
        db.add_user(1, "Alice")
        assert db.get_user(1) == "Alice"
        
    def test_add_duplicate_user(db):
        db.add_user(1, "Alice")
        with pytest.raises(ValueError,match="user alredy exists"):
            db.add_user(1, "Bob")
            assert db.get_user(2) is None