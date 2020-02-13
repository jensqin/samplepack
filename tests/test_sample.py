import pytest
import json

from samplepack.sample01 import add_one
from samplepack.sample02.sample02 import add_two


with open("tests/data/sample.json") as jsonfile:
    inputs = json.load(jsonfile)


def test_load_data():
    assert 0 == inputs["set"]


def test_add_one():
    res = add_one(0)
    assert res == 1


def test_add_two():
    res = add_two(0)
    assert res == 2
