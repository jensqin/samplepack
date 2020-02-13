"""The sample01.py module.

This module has a function called add_one.

"""

from samplepack.settings import prstat

# function definition.


def add_one(n):
    """
    add_one(n)

    The sum of a number and one.

    Parameters
    __________
    n : int
        The input number.

    Returns
    _______
    int
        The value :math:`n + 1`.
    """

    print(prstat)
    return n + 1


if __name__ == "__main__":
    print("hello world 1")
