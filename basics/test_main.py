from basics.main import get_weather, add, divide
import pytest

def test_get_weather():
    assert get_weather(21) == 'hot'



def test_add():
    assert add(2, 3) == 5, "sum 5"
    assert add(-1, 1) == 0, "sum 0"
    assert add(0, 0) == 0, "sum 0"
    
    
def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        assert divide(10, 0)