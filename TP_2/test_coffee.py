import pytest
from BuilderFactory import build_beverage, pretty_description


def main():
    test_espresso_double_mocha_caramel()
    test_houseblend_soy_whip()
    test_darkroast_triple_whip()
    test_invalid_base()
    test_invalid_condiment()


def test_espresso_double_mocha_caramel():
    """
    Espresso grande con doble Mocha y Caramel
    """
    bev = build_beverage("Espresso", "G", ["Mocha", "Mocha", "Caramel"])
    expected_cost = 1.99 + 0.20 * 2 + 0.20
    assert abs(bev.cost() - expected_cost) < 1e-6
    assert "Double Mocha" in pretty_description(bev)
    assert "Caramel" in pretty_description(bev)


def test_houseblend_soy_whip():
    """
    HouseBlend mediano con Soja y Crema
    """
    bev = build_beverage("HouseBlend", "M", ["Soy", "Whip"])
    expected_cost = 0.89 + (0.15 * 1.10) + 0.10
    assert abs(bev.cost() - expected_cost) < 1e-6
    desc = pretty_description(bev)
    assert "Café de la Casa" in desc
    assert "Soja" in desc
    assert "Crema" in desc


def test_darkroast_triple_whip():
    """
    DarkRoast pequeño con triple Crema
    """
    bev = build_beverage("DarkRoast", "P", ["Whip", "Whip", "Whip"])
    expected_cost = 0.99 * 1 + 0.10 * 3
    assert abs(bev.cost() - expected_cost) < 1e-6
    assert "Triple Crema" in pretty_description(bev)


def test_invalid_base():
    """
    Intentar una base inexistente debería lanzar ValueError
    """
    with pytest.raises(ValueError) as excinfo:
        build_beverage("Latte", "Mediano", [])
    assert "Base 'Latte' no encontrada" in str(excinfo.value)


def test_invalid_condiment():
    """
    Intentar un condimento inexistente debería lanzar ValueError
    """
    with pytest.raises(ValueError) as excinfo:
        build_beverage("Espresso", "M", ["Honey"])
    assert "Condimento 'Honey' no encontrado" in str(excinfo.value)


if __name__ == "__main__":
    pytest.main()