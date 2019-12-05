import pytest 
from sample.sample01.sample01 import func_one
import sample.sample01 as sample01 
import sample.sample02 as sample02


def test_pack():
    assert func_one() == 1
