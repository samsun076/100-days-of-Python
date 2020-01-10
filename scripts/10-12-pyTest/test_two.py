# playing with pyTest
# initial explopration is with additional resource
# python testing with PyTest book

# This is from the getting pytest section of  book.


def test_failing():
    assert (1,2,3,) == (3,2,1)