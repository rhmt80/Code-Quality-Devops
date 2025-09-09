# tests/test_calculator.py

import pytest
from my_module.calculator import add, subtract


def test_add():
    """Tests the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0


def test_add_type_error():
    """Tests that add raises TypeError for non-numeric input."""
    with pytest.raises(TypeError):
        add('a', 3)
    with pytest.raises(TypeError):
        add(2, 'b')


def test_subtract():
    """Tests the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(1, 5) == -4
    assert subtract(2.5, 1.5) == 1.0
