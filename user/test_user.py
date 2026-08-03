import pytest
from user.user import UserManager


@pytest.fixture
def user_manager():
    """create a freash instance of UserManager before each test """
    return UserManager()

# user_manager = UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("adem_kaba", "akabayel@example.com") == True
    assert user_manager.get_user("adem_kaba") == "akabayel@example.com"
    
def test_add_duplicate_user(user_manager):
    user_manager.add_user("adem_kaba", "akabayel@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("adem_kaba", "akabayel@example.com")