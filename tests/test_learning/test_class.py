import pytest


@pytest.mark.learning
class TestClass:
    value = 0

    def test_one(self):
        print('test_one')
        self.value = 1
        assert self.value == 1

    def test_two(self):
        print('test_two')
        assert self.value == 1


if __name__ == '__main__':
    pytest.main()
