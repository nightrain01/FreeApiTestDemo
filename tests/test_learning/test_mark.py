import pytest


@pytest.mark.learning
@pytest.mark.mycustom
def test_mark():
    print('test_mark')
    assert True


@pytest.mark.learning
@pytest.mark.notmycustom
def test_mark2():
    print('test_mark2')
    assert True


if __name__ == '__main__':
    pytest.main()
