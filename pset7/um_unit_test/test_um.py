import pytest
from um import count


def test_count_default():
    with pytest.raises(TypeError):
        count()


def test_count_blank():
    assert count("") == 0


def test_count_disregard():
    assert count("yummy") == 0
    assert count("   yummy") == 0
    assert count("yummy   ") == 0
    assert count("umre") == 0
    assert count(" umre") == 0
    assert count("umre ") == 0


def test_count_proper():
    assert count("um") == 1
    assert count(" Um, thanks for the album.") == 1
    assert count("um ") == 1
    assert count(" UM ") == 1
    assert count("um?") == 1
    assert count("Um... thanks, um...") == 2
    assert count("um    um,  um. um um   yummy   um  um?>?  um?  umre  um") == 9
