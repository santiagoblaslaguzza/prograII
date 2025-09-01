"""
Testing correspondiente a la clase Beverage y sus subclases.
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from beverages import Espresso


def test_set_size_should_modify_beverage_size():
    """Test para verificar que se puede modificar el tamaño de una bebida"""
    beverage = Espresso()
    beverage.set_size("Grande")
    assert beverage.get_size() == "Grande"


def test_set_size_should_not_allow_invalid_size():
    """Test para verificar que no se puede modificar el tamaño de una bebida a un tamaño inválido"""
    beverage = Espresso()
    with pytest.raises(ValueError):
        beverage.set_size("gigante")

