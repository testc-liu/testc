# Automatically generated by Pynguin.
import main as module_0


def test_case_0():
    int_0 = -2183
    int_1 = -726
    list_0 = [int_0, int_1, int_1]
    bool_0 = module_0.below_zero(list_0)
    assert bool_0 is True


def test_case_1():
    list_0 = []
    bool_0 = module_0.below_zero(list_0)
    bool_1 = module_0.below_zero(list_0)


def test_case_2():
    int_0 = 2369
    int_1 = -1450
    list_0 = [int_0, int_0, int_1]
    bool_0 = module_0.below_zero(list_0)
    assert bool_0 is False
    list_1 = [int_0]
    bool_1 = module_0.below_zero(list_1)
    assert bool_1 is False
