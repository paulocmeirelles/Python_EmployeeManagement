import pytest
from app.main.helpers.app_helper import arrayMoto

def test_helper_arrayMoto(arrayMoto):
    assert isinstance(arrayMoto,(list))