# Automatically generated by Pynguin.
import pytest
import main as module_0


def test_case_0():
    str_0 = "pj>a$\x0bE&wniVrsk``X3"
    list_0 = module_0.separate_paren_groups(str_0)


def test_case_1():
    str_0 = "x/10r'G`9!"
    str_1 = '_RG|.Bb!"A+O(^}t'
    list_0 = module_0.separate_paren_groups(str_1)
    list_1 = module_0.separate_paren_groups(str_0)
    list_2 = module_0.separate_paren_groups(str_0)
    str_2 = "8 "
    list_3 = module_0.separate_paren_groups(str_2)
    list_4 = module_0.separate_paren_groups(str_0)


def test_case_2():
    str_0 = "W\n"
    list_0 = module_0.separate_paren_groups(str_0)
    str_1 = "xfR>n),51>ny^Yh>3\\"
    list_1 = module_0.separate_paren_groups(str_1)
    assert list_1 == []
    list_2 = module_0.separate_paren_groups(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "N27()0s^#\x0c8sDPk>[Q"
    list_0 = module_0.separate_paren_groups(str_0)
    assert list_0 == ["()"]
    list_1 = module_0.separate_paren_groups(str_0)
    assert list_1 == ["()"]
    none_type_0 = None
    list_2 = module_0.separate_paren_groups(str_0)
    assert list_2 == ["()"]
    module_0.separate_paren_groups(none_type_0)
