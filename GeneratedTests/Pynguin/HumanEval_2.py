# Automatically generated by Pynguin.
import pytest
import main as module_0


def test_case_0():
    float_0 = -3868.6005
    float_1 = module_0.truncate_number(float_0)
    assert float_1 == pytest.approx(0.3994999999999891, abs=0.01, rel=0.01)