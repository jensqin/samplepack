import pytest 
import json
from samplepack.sample01.sample01 import func_one
import samplepack.sample02 as sample02


with open('data/sample.json') as jsonfile:
    inputs = json.load(jsonfile)

def test_pack():
    assert func_one() == inputs['set']
