import pytest

from src.Circle import Circle

@pytest.fixture
def def_circe():
    circle=Circle(10)
    yield circle
    del circle