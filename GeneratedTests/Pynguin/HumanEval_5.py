# Automatically generated by Pynguin.
import main as module_0


def test_case_0():
    int_0 = -1536
    list_0 = [int_0, int_0, int_0]
    int_1 = 10
    list_1 = module_0.intersperse(list_0, int_1)
    assert list_1 == [-1536, 10, -1536, 10, -1536]


def test_case_1():
    list_0 = []
    int_0 = -1096
    list_1 = module_0.intersperse(list_0, int_0)
    assert list_1 == []
    none_type_0 = None
    int_1 = -372
    list_2 = module_0.intersperse(none_type_0, int_1)
    assert list_2 == []
