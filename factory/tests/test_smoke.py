def test_imports():
    import factory.simple_factory.main as s
    import factory.factory_method.main as fm
    import factory.abstract_factory.main as af
    assert callable(s.main) and callable(fm.main) and callable(af.main)
