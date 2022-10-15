import pytest

import checkarg.dict as Dict
from checkarg.exceptions import ArgumentError

one_element = {"a": 1}
three_elements = {"a": 1, "b": 2, "c": 3}
seven_int_values_elements = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6}
seven_str_values_elements = {
    "a": "a",
    "b": "b",
    "c": "c",
    "d": "d",
    "e": "e",
    "f": "f",
    "g": "g",
}
three_mix = {"a": 0, "b": "1", "c": 3.0}
seven_mix = {"a": 0, "b": "1", "c": [2], "d": 3.0, "e": {4: 4}, "f": (5, 0), "g": True}

empty_dicts = [pytest.param({}, id="Empty dict"), pytest.param(None, id="None dict")]

not_empty_dicts = [
    pytest.param(one_element, id="Dict 1 item"),
    pytest.param(seven_int_values_elements, id="Dict 7 int values"),
    pytest.param(seven_str_values_elements, id="Dict 7 str values"),
    pytest.param(seven_mix, id="Dict 7 mix"),
]

dicts_with_length_lower_than_3 = [
    pytest.param({}, id="Empty dict"),
    pytest.param(one_element, id="Dict 1 item"),
    pytest.param({"a": 0, "b": 1}, id="Dict 2 items"),
    pytest.param({"a": 0, "b": "1"}, id="Dict 2 mix"),
]

dicts_with_length_greater_than_5 = [
    pytest.param(seven_int_values_elements, id="Dict 7 items"),
    pytest.param(seven_str_values_elements, id="Dict 7 items"),
    pytest.param(seven_mix, id="Dict 7 mix"),
]

dicts_with_length_equals_to_7 = [
    pytest.param(seven_int_values_elements, id="Dict 7 items"),
    pytest.param(seven_str_values_elements, id="Dict 7 items"),
    pytest.param(seven_mix, id="Dict 7 mix"),
]

dicts_with_length_between_3_and_5 = [
    pytest.param({"a": 0, "b": 1, "c": 2}, id="Dict 3 items"),
    pytest.param({"a": 0, "b": 1, "c": 2, "d": None}, id="Dict 4 items"),
]


@pytest.mark.parametrize("dict", not_empty_dicts)
def test_is_empty__with_items__does_nothing(dict):
    # Arrange & Act & Assert
    Dict.is_not_empty(dict)


@pytest.mark.parametrize("dict", empty_dicts)
def test_is_empty_with_no_elements_raise_exception(dict):
    with pytest.raises(ArgumentError):
        Dict.is_not_empty(dict)


@pytest.mark.parametrize("dict", dicts_with_length_lower_than_3)
def test_has_length_lower__with_length_lower_3__does_nothing(dict):
    # Arrange & Act & Assert
    Dict.has_length_lower(dict, 3)


@pytest.mark.parametrize("dict", dicts_with_length_greater_than_5)
def test_has_length_lower__with_length_greater_3__raise_exception(dict):
    with pytest.raises(ArgumentError):
        Dict.has_length_lower(dict, 5)


@pytest.mark.parametrize("dict", dicts_with_length_greater_than_5)
def test_has_length_greater__with_length_greater_5__does_nothing(dict):
    # Arrange & Act & Assert
    Dict.has_length_greater(dict, 5)


@pytest.mark.parametrize("dict", dicts_with_length_lower_than_3)
def test_has_length_greater__with_length_lower_5__raise_exception(dict):
    with pytest.raises(ArgumentError):
        Dict.has_length_greater(dict, 3)


@pytest.mark.parametrize("dict", dicts_with_length_between_3_and_5)
def test_has_length_between__with_length_between_3_5__does_nothing(dict):
    # Arrange & Act & Assert
    Dict.has_length_between(dict, 3, 5)


@pytest.mark.parametrize("dict", dicts_with_length_lower_than_3)
def test_has_length_between__with_length_lower_than_3__raise_exception(dict):
    with pytest.raises(ArgumentError):
        Dict.has_length_between(dict, 3, 5)


@pytest.mark.parametrize("dict", dicts_with_length_greater_than_5)
def test_has_length_between__with_length_greater_than_5__raise_exception(dict):
    with pytest.raises(ArgumentError):
        Dict.has_length_between(dict, 3, 5)


@pytest.mark.parametrize("dict", dicts_with_length_equals_to_7)
def test_is_length_equals__with_length_equal_7__does_nothing(dict):
    # Arrange & Act & Assert
    Dict.is_length_equals(dict, 7)


@pytest.mark.parametrize("dict", dicts_with_length_lower_than_3)
def test_is_length_equals__with_length_lower_than_3__raise_exception(dict):
    with pytest.raises(ArgumentError):
        Dict.is_length_equals(dict, 3)


@pytest.mark.parametrize(
    "dict, element_in_dict",
    [(seven_mix, {"a": 0}), (seven_mix, {"c": [2]}), (seven_mix, {"d": 3.0})],
)
def test_contains__with_element_in_dict__does_nothing(dict, element_in_dict):
    # Arrange & Act & Assert
    Dict.contains(dict, element_in_dict)


@pytest.mark.parametrize(
    "dict, element_in_dict",
    [(three_mix, {"a": 1}), (three_mix, {"c": [2]}), (three_mix, {"d": 3.0})],
)
def test_contains__with_element_not_in_dict__raise_exception(dict, element_in_dict):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Dict.contains(dict, element_in_dict)


@pytest.mark.parametrize(
    "dict, element_in_dict", [(seven_mix, "a"), (seven_mix, "c"), (seven_mix, "d")]
)
def test_contains_key__with_element_in_dict__does_nothing(dict, element_in_dict):
    # Arrange & Act & Assert
    Dict.contains_key(dict, element_in_dict)


@pytest.mark.parametrize(
    "dict, element_in_dict", [(three_mix, "z"), (three_mix, 111), (three_mix, "A")]
)
def test_contains_key__with_element_not_in_dict__raise_exception(dict, element_in_dict):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Dict.contains_key(dict, element_in_dict)
