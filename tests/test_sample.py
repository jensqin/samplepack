import pytest 
from samplepack.sample01.sample01 import func_one
import samplepack.sample02 as sample02


def test_pack():
    assert func_one() == 1
