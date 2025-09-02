"""
Testing correspondiente a la impresion decorada
"""

import pytest
import sys
import os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from beverages import * #Espresso, HouseBlend, DarkRoast, Decaf
from condiments import * #Milk, Mocha, Soy, Whip, Caramel
from pretty_print import impresion

# ========== TESTS BÁSICOS DE IMPRESION DECORADA ==========


class TestImpresionDecorada:
    """Tests para distintos combinaciones sin condimentos condimentos repetidos y/o combinados"""
    @pytest.mark.parametrize(
        "condiment_sequence, expected_text",
        [
            ([Whip], "Espresso, Crema"),
            ([Whip, Mocha, Mocha], "Espresso, Crema, Double Mocha"),
            ([Mocha, Mocha, Whip],  "Espresso, Double Mocha, Crema"),
            ([Whip, Mocha, Caramel],  "Espresso, Crema, Mocha, Caramelo"),
            ([Mocha, Mocha, Mocha, Mocha], "Espresso, 4x Mocha"),
            ([Soy, Soy, Soy, Soy, Soy], "Espresso, 5x Soja"),
            ([Mocha, Mocha, Mocha, Mocha, Caramel], "Espresso, 4x Mocha, Caramelo"),

        ],
    )
    def test_condiment_combinations_should_correct_pretty_print(
        self, condiment_sequence, expected_text
    ):
        """Test parametrizado para diferentes combinaciones de condimentos"""
        espresso = Espresso()
        decorated = espresso

        # Aplicar condimentos en secuencia
        for condiment_class in condiment_sequence:
            decorated = condiment_class(decorated)
        impresion(decorated.get_description())
     #   assert decorated.cost() == pytest.approx(expected_cost, abs=0.01)
      #  assert milk_beverage.get_description() == f"{base_description}, Leche"
        assert impresion(decorated.get_description()) == expected_text






