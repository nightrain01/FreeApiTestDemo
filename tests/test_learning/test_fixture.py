import pytest


@pytest.mark.learning
@pytest.mark.usefixtures('fixture_function', 'fixture_class', 'fixture_module', 'fixture_package', 'fixture_session')
class TestFixture:

    def test_fixture1(self):
        print('test_fixture1')
        assert True

    def test_fixture2(self):
        print('test_fixture2')
        assert True

    def test_fixture3(self):
        print('test_fixture3')
        assert True
