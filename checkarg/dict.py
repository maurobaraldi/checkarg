from typing import Dict, TypeVar

import checkarg.none_type as NoneType
from checkarg.exceptions import ArgumentError, DictErrorMessages

T = TypeVar("T")


def is_not_empty(
    dict: Dict, argument_name: str = None, exception: Exception = None
) -> None:
    """ Check if the given dict is not empty """
    NoneType.is_not_none(dict, argument_name, exception)
    if not dict:
        raise ArgumentError(
            DictErrorMessages.is_not_empty_message(argument_name), argument_name
        ) if exception is None else exception


def has_length_lower(
    dict: Dict,
    condition_value: int,
    argument_name: str = None,
    exception: Exception = None,
) -> None:
    """ Check if the given dict length is lower than the condition_value """
    NoneType.is_not_none(dict, argument_name, exception)
    if len(dict) >= condition_value:
        raise ArgumentError(
            DictErrorMessages.has_length_lower_message(argument_name, condition_value),
            argument_name,
        ) if exception is None else exception


def has_length_greater(
    dict: Dict,
    condition_value: int,
    argument_name: str = None,
    exception: Exception = None,
) -> None:
    """ Check if the given dict length is greater than the condition_value """
    NoneType.is_not_none(dict, argument_name, exception)
    if len(dict) <= condition_value:
        raise ArgumentError(
            DictErrorMessages.has_length_greater_message(
                argument_name, condition_value
            ),
            argument_name,
        ) if exception is None else exception


def has_length_between(
    dict: Dict,
    min_length: int,
    max_length: int,
    argument_name: str = None,
    exception: Exception = None,
) -> None:
    """ Check if the given dict length is between min_length and max_length """

    has_length_greater(dict, min_length - 1, argument_name, exception)
    has_length_lower(dict, max_length + 1, argument_name, exception)


def is_length_equals(
    dict: Dict,
    condition_value: int,
    argument_name: str = None,
    exception: Exception = None,
) -> None:
    """ Check if the given dict length is equals than the condition_value """
    NoneType.is_not_none(dict, argument_name, exception)
    if len(dict) != condition_value:
        raise ArgumentError(
            DictErrorMessages.has_length_equals_message(argument_name, condition_value),
            argument_name,
        ) if exception is None else exception


def contains(
    dict: Dict, element: Dict, argument_name: str = None, exception: Exception = None
) -> None:
    """ Check if a given element is present in the dict """
    NoneType.is_not_none(dict, argument_name, exception)
    if not element.items() <= dict.items():
        raise ArgumentError(
            DictErrorMessages.contains_message(argument_name, element), argument_name
        ) if exception is None else exception


def contains_key(
    dict: Dict, element: T, argument_name: str = None, exception: Exception = None
) -> None:
    """ Check if a given element (key) is present in the dict """
    NoneType.is_not_none(dict, argument_name, exception)
    if element not in dict:
        raise ArgumentError(
            DictErrorMessages.contains_key(argument_name, element), argument_name
        ) if exception is None else exception
