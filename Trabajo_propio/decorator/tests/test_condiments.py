"""
Testing correspondiente a la clase CondimentDecorator y sus subclases.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from beverages import Espresso, HouseBlend, DarkRoast, Decaf
from condiments import Milk, Mocha, Soy, Whip, Caramel


# ========== TESTS BÁSICOS DE CONDIMENTOS INDIVIDUALES ==========


class TestSingleCondiments:
    """Tests para condimentos individuales aplicados a bebidas base"""

    @pytest.mark.parametrize(
        "beverage_class,base_cost,base_description",
        [
            (Espresso, 1.99, "Espresso"),
            (HouseBlend, 0.89, "Café de la Casa"),
            (DarkRoast, 0.99, "Café Dark Roast"),
            (Decaf, 1.05, "Café Descafeinado"),
        ],
    )
    def test_milk_should_add_010_cost_when_applied_to_any_beverage(
        self, beverage_class, base_cost, base_description
    ):
        """Test que verifica que Milk agrega $0.10 al costo base"""
        beverage = beverage_class()
        milk_beverage = Milk(beverage)

        assert milk_beverage.cost() == base_cost + 0.10
        assert milk_beverage.get_description() == f"{base_description}, Leche"

    @pytest.mark.parametrize(
        "beverage_class,base_cost,base_description",
        [
            (Espresso, 1.99, "Espresso"),
            (HouseBlend, 0.89, "Café de la Casa"),
            (DarkRoast, 0.99, "Café Dark Roast"),
            (Decaf, 1.05, "Café Descafeinado"),
        ],
    )
    def test_mocha_should_add_020_cost_when_applied_to_any_beverage(
        self, beverage_class, base_cost, base_description
    ):
        """Test que verifica que Mocha agrega $0.20 al costo base"""
        beverage = beverage_class()
        mocha_beverage = Mocha(beverage)

        assert mocha_beverage.cost() == base_cost + 0.20
        assert mocha_beverage.get_description() == f"{base_description}, Mocha"

    @pytest.mark.parametrize(
        "beverage_class,base_cost,base_description",
        [
            (Espresso, 1.99, "Espresso"),
            (HouseBlend, 0.89, "Café de la Casa"),
            (DarkRoast, 0.99, "Café Dark Roast"),
            (Decaf, 1.05, "Café Descafeinado"),
        ],
    )
    def test_whip_should_add_010_cost_when_applied_to_any_beverage(
        self, beverage_class, base_cost, base_description
    ):
        """Test que verifica que Whip agrega $0.10 al costo base"""
        beverage = beverage_class()
        whip_beverage = Whip(beverage)

        assert whip_beverage.cost() == base_cost + 0.10
        assert whip_beverage.get_description() == f"{base_description}, Crema"

    @pytest.mark.parametrize(
        "beverage_class,base_cost,base_description",
        [
            (Espresso, 1.99, "Espresso"),
            (HouseBlend, 0.89, "Café de la Casa"),
            (DarkRoast, 0.99, "Café Dark Roast"),
            (Decaf, 1.05, "Café Descafeinado"),
        ],
    )
    def test_caramel_should_add_020_cost_when_applied_to_any_beverage(
        self, beverage_class, base_cost, base_description
    ):
        """Test que verifica que Caramel agrega $0.20 al costo base"""
        beverage = beverage_class()
        caramel_beverage = Caramel(beverage)

        assert caramel_beverage.cost() == base_cost + 0.20
        assert caramel_beverage.get_description() == f"{base_description}, Caramelo"


# ========== TESTS DE SOY CON DIFERENTES TAMAÑOS ==========


class TestSoyWithSizes:
    """Tests específicos para Soy que tiene precios variables según tamaño"""

    @pytest.mark.parametrize(
        "size,expected_soy_cost", [("Tall", 0.10), ("Grande", 0.15), ("Venti", 0.20)]
    )
    def test_soy_should_add_size_specific_cost_when_applied_to_beverage(
        self, size, expected_soy_cost
    ):
        """Test que verifica que Soy agrega costo según el tamaño de la bebida"""
        espresso = Espresso()
        espresso.set_size(size)
        soy_espresso = Soy(espresso)

        expected_total = 1.99 + expected_soy_cost
        assert soy_espresso.cost() == expected_total
        assert soy_espresso.get_description() == "Espresso, Soja"


# ========== TESTS DE MÚLTIPLES DECORADORES ==========


class TestMultipleDecorators:
    """Tests para combinaciones de múltiples condimentos"""

    def test_multiple_condiments_should_stack_costs_when_applied_sequentially(self):
        """Test que verifica que múltiples condimentos apilan sus costos correctamente"""
        # Espresso base: $1.99
        espresso = Espresso()
        decorated = Mocha(Milk(Whip(espresso)))  # +0.20 +0.10 +0.10

        expected_cost = 1.99 + 0.20 + 0.10 + 0.10  # 2.39
        expected_description = "Espresso, Crema, Leche, Mocha"

        assert decorated.cost() == expected_cost
        assert decorated.get_description() == expected_description

    def test_double_condiment_should_double_cost_when_applied_twice(self):
        """Test que verifica que aplicar el mismo condimento dos veces duplica su costo"""
        espresso = Espresso()
        double_mocha = Mocha(Mocha(espresso))

        expected_cost = 1.99 + 0.20 + 0.20  # 2.39
        expected_description = "Espresso, Mocha, Mocha"

        assert double_mocha.cost() == expected_cost
        assert double_mocha.get_description() == expected_description

    def test_complex_combination_should_calculate_correctly_when_multiple_condiments_applied(
        self,
    ):
        """Test para una combinación compleja de múltiples condimentos"""
        # HouseBlend + Soy + Mocha + Whip (como en el README)
        house_blend = HouseBlend()
        house_blend.set_size("Tall")  # Soy Tall = +0.10
        complex_drink = Whip(Mocha(Soy(house_blend)))

        expected_cost = 0.89 + 0.10 + 0.20 + 0.10  # 1.29
        expected_description = "Café de la Casa, Soja, Mocha, Crema"

        assert complex_drink.cost() == expected_cost
        assert complex_drink.get_description() == expected_description

    @pytest.mark.parametrize(
        "condiment_sequence,expected_addition",
        [
            ([Milk], 0.10),
            ([Milk, Mocha], 0.30),
            ([Milk, Mocha, Whip], 0.40),
            ([Milk, Mocha, Whip, Caramel], 0.60),
            ([Mocha, Mocha], 0.40),
            ([Milk, Milk, Milk], 0.30),
        ],
    )
    def test_condiment_combinations_should_sum_correctly_when_applied_to_espresso(
        self, condiment_sequence, expected_addition
    ):
        """Test parametrizado para diferentes combinaciones de condimentos"""
        espresso = Espresso()
        decorated = espresso

        # Aplicar condimentos en secuencia
        for condiment_class in condiment_sequence:
            decorated = condiment_class(decorated)

        expected_cost = 1.99 + expected_addition
        assert decorated.cost() == pytest.approx(expected_cost, abs=0.01)


# ========== TESTS DE INTEGRIDAD DEL PATRÓN DECORATOR ==========


class TestDecoratorPatternIntegrity:
    """Tests que verifican que el patrón Decorator funciona correctamente"""

    def test_decorated_beverage_should_maintain_beverage_interface_when_decorated(self):
        """Test que verifica que las bebidas decoradas mantienen la interfaz Beverage"""
        from beverages import Beverage

        espresso = Espresso()
        decorated = Mocha(Milk(espresso))

        # Debe seguir siendo una instancia de Beverage
        assert isinstance(decorated, Beverage)

        # Debe tener los métodos requeridos
        assert hasattr(decorated, "cost")
        assert hasattr(decorated, "get_description")
        assert hasattr(decorated, "get_size")
        assert hasattr(decorated, "set_size")

    def test_size_should_propagate_correctly_when_beverage_is_decorated(self):
        """Test que verifica que el tamaño se propaga correctamente en bebidas decoradas"""
        espresso = Espresso()
        espresso.set_size("Grande")

        decorated = Mocha(Milk(espresso))

        # El tamaño debe propagarse al decorador
        assert decorated.size == "Grande"

    def test_nested_decorators_should_maintain_original_beverage_reference_when_deeply_nested(
        self,
    ):
        """Test que verifica que los decoradores anidados mantienen referencia a la bebida original"""
        espresso = Espresso()
        deeply_decorated = Caramel(Whip(Mocha(Milk(espresso))))

        # Debería poder acceder a la bebida original a través de la cadena
        current = deeply_decorated
        while hasattr(current, "_beverage"):
            current = current._beverage

        assert isinstance(current, Espresso)
        assert current.get_description() == "Espresso"


# ========== TESTS DE CASOS EDGE ==========


class TestEdgeCases:
    """Tests para casos límite y situaciones especiales"""

    def test_condiment_should_work_correctly_when_applied_to_already_decorated_beverage(
        self,
    ):
        """Test que verifica que se puede decorar una bebida ya decorada"""
        espresso = Espresso()
        first_decoration = Milk(espresso)
        second_decoration = Mocha(first_decoration)

        assert second_decoration.cost() == 1.99 + 0.10 + 0.20
        assert second_decoration.get_description() == "Espresso, Leche, Mocha"

    def test_soy_with_venti_size_should_cost_most_when_compared_to_other_sizes(self):
        """Test que verifica que Soy con tamaño Venti es el más caro"""
        espresso_tall = Espresso()
        espresso_tall.set_size("Tall")
        soy_tall = Soy(espresso_tall)

        espresso_grande = Espresso()
        espresso_grande.set_size("Grande")
        soy_grande = Soy(espresso_grande)

        espresso_venti = Espresso()
        espresso_venti.set_size("Venti")
        soy_venti = Soy(espresso_venti)

        assert soy_venti.cost() > soy_grande.cost() > soy_tall.cost()
