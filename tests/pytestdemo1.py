import sys

import pytest

sys.path.append('/path/to/folder')


@pytest.fixture
def example_fixture():
    return 1


def test_with_fixture(example_fixture):
    assert example_fixture == 1
