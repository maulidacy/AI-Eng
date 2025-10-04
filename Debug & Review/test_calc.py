from CLI_Sederhana.calc_cli import add_sub, mul, div
import pytest

def test_add():
    assert add(2,3) == 5

def test_div_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        div(1,0)