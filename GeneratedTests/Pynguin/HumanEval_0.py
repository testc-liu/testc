# Automatically generated by Pynguin.
import pytest
import main as module_0


def test_case_0():
    none_type_0 = None
    list_0 = [none_type_0]
    bool_0 = module_0.has_close_elements(list_0, none_type_0)
    assert bool_0 is False


def test_case_1():
    list_0 = []
    float_0 = -374.0
    bool_0 = module_0.has_close_elements(list_0, float_0)
    assert bool_0 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    float_0 = -724.8
    list_0 = [none_type_0, none_type_0, float_0, float_0]
    float_1 = -452.527
    module_0.has_close_elements(list_0, float_1)


def test_case_3():
    float_0 = -3875.508308
    list_0 = [float_0]
    bool_0 = module_0.has_close_elements(list_0, float_0)
    assert bool_0 is False
    float_1 = -3255.0
    float_2 = 363.0
    list_1 = [float_0, float_2, float_2]
    bool_1 = module_0.has_close_elements(list_1, float_2)
    assert bool_1 is True
    bool_2 = module_0.has_close_elements(list_0, float_1)
    assert bool_2 is False


def test_case_4():
    float_0 = -2162.0977
    float_1 = 488.877
    list_0 = [float_0]
    float_2 = -426.29
    bool_0 = module_0.has_close_elements(list_0, float_2)
    assert bool_0 is False
    list_1 = [float_0, float_1]
    bool_1 = module_0.has_close_elements(list_1, float_0)
    assert bool_1 is False
