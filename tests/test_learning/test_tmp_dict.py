import pytest


@pytest.mark.learning
def test_tmp_dict(tmp_path):
    print(tmp_path)
    assert tmp_path.exists()
