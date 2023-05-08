from .first import add_numbers, concat_strings


def test_passing():
    x = 1, 2, 3
    y = 1, 2, 3
    assert x == y


# def test_failing():
#     x = 1, 2, 3
#     y = 1, 2, 4
#     assert x == y


def test_add_numbers():
    x, y = 3, 4
    assert add_numbers(x, y) == 7


def test_concat_strings():
    a, b = "hello ", "world"
    assert concat_strings(a, b) == "hello world"


def test_item_in_list():
    items = [1, 2, 3]
    assert 1 in items


def test_item_is_not_none():
    item = "foobar"
    assert item is not None
