"""module 1"""

def add(x, y):
    """
    Add x + y
    >>> add(2, 3)
    5
    """
    return x + y
    """All futher comments will be ignorred"""


# pydoc -w test_function
# html file will be generated

# python -m doctest test_function.py
# python -m doctest test_function.py -v

# CI for Python - buildbot
