"""The runner.py module.

This module is only for running functions.

"""

from samplepack.sample01 import sample01
from samplepack.sample02 import sample02

if __name__ == "__main__":
    print('1 + 1 = ')
    print(sample01.add_one(1))
