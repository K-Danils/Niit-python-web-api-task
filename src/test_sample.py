import pytest
from reading_statistics import *

readings_examples = [
    [
        (
            1,
            20,
            "15/3/2022"
        ),
        (
            2,
            30,
            "15/3/2022"
        ),
        (
            3,
            15,
            "16/3/2022"
        ),
        (
            4,
            49.9,
            "8/3/2022"
        ),
        (
            5,
            5,
            "8/3/2022"
        )
    ],
    [
        (
            5,
            1330,
            "15/3/2022"
        ),
        (
            2,
            -15,
            "15/3/2022"
        ),
        (
            3,
            6.108,
            "16/3/2022"
        ),
        (
            4,
            10999,
            "8/3/2022"
        ),
        (
            5,
            0,
            "8/3/2022"
        )
    ],
    ]

def test_method_get_readings_mean():
    assert get_readings_mean(readings_examples[0]) == 23.98
    assert get_readings_mean(readings_examples[1]) == 2464.0216

def test_method_get_readings_variance():
    assert get_readings_variance(readings_examples[0]) == 291.202
    assert get_readings_variance(readings_examples[1]) == 23097537.7703328
