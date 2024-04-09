import pytest


@pytest.mark.learning
@pytest.mark.usefixtures('fixture_function', 'fixture_class', 'fixture_module', 'fixture_package', 'fixture_session')
class TestFixture1:

    def test_fixture1(self):
        print('test_fixture1')
        assert True

    def test_fixture2(self):
        print('test_fixture2')
        assert True

    def test_fixture3(self):
        print('test_fixture3')
        assert True


@pytest.mark.learning
@pytest.mark.usefixtures('fixture_function', 'fixture_class', 'fixture_module', 'fixture_package', 'fixture_session')
class TestFixture2:

    def test_fixture1(self):
        print('test_fixture1')
        assert True

    def test_fixture2(self):
        print('test_fixture2')
        assert True

    def test_fixture3(self):
        print('test_fixture3')
        assert True


if __name__ == '__main__':
    pytest.main()
