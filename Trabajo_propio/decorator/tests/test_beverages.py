"""
Testing correspondiente a la clase Beverage y sus subclases.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from beverages import Espresso, HouseBlend, DarkRoast, Decaf, Beverage


# ========== TESTS BÁSICOS DE BEBIDAS ==========


class TestBeverageBasics:
    """Tests básicos para todas las bebidas"""

    @pytest.mark.parametrize(
        "beverage_class,expected_description,expected_cost",
        [
            (Espresso, "Espresso", 1.99),
            (HouseBlend, "Café de la Casa", 0.89),
            (DarkRoast, "Café Dark Roast", 0.99),
            (Decaf, "Café Descafeinado", 1.05),
        ],
    )
    def test_beverage_should_have_correct_description_and_cost_when_created(
        self, beverage_class, expected_description, expected_cost
    ):
        """Test parametrizado que verifica descripción y costo de cada bebida"""
        beverage = beverage_class()

        assert beverage.get_description() == expected_description
        assert beverage.cost() == expected_cost

    @pytest.mark.parametrize("beverage_class", [Espresso, HouseBlend, DarkRoast, Decaf])
    def test_beverage_should_start_with_tall_size_when_created(self, beverage_class):
        """Test que verifica que todas las bebidas inician con tamaño Tall"""
        beverage = beverage_class()
        assert beverage.get_size() == "Tall"

    @pytest.mark.parametrize("beverage_class", [Espresso, HouseBlend, DarkRoast, Decaf])
    def test_beverage_subtype_should_be_instance_of_beverage_when_created(
        self, beverage_class
    ):
        """Test que verifica que todas las bebidas son instancias de Beverage"""
        beverage = beverage_class()
        assert isinstance(beverage, Beverage)


# ========== TESTS DE TAMAÑOS ==========


class TestBeverageSizes:
    """Tests para funcionalidad de tamaños de bebidas"""

    @pytest.mark.parametrize("beverage_class", [Espresso, HouseBlend, DarkRoast, Decaf])
    @pytest.mark.parametrize("size", ["Tall", "Grande", "Venti"])
    def test_set_size_should_modify_beverage_size_when_valid_size_provided(
        self, beverage_class, size
    ):
        """Test parametrizado que verifica que se puede modificar el tamaño de cualquier bebida"""
        beverage = beverage_class()
        beverage.set_size(size)
        assert beverage.get_size() == size

    @pytest.mark.parametrize("beverage_class", [Espresso, HouseBlend, DarkRoast, Decaf])
    @pytest.mark.parametrize(
        "invalid_size",
        ["gigante", "pequeño", "mediano", "", "TALL", "grande", None, 123],
    )
    def test_set_size_should_raise_error_when_invalid_size_provided(
        self, beverage_class, invalid_size
    ):
        """Test parametrizado que verifica que no se puede usar un tamaño inválido"""
        beverage = beverage_class()
        with pytest.raises(ValueError, match="Tamaño no disponible"):
            beverage.set_size(invalid_size)

    @pytest.mark.parametrize("beverage_class", [Espresso, HouseBlend, DarkRoast, Decaf])
    def test_get_available_sizes_should_return_correct_sizes_when_called(
        self, beverage_class
    ):
        """Test que verifica que todas las bebidas devuelven los tamaños disponibles correctos"""
        beverage = beverage_class()
        expected_sizes = ["Tall", "Grande", "Venti"]
        assert beverage.get_available_sizes() == expected_sizes
