from .. import repeat_string


def test_repeat_string():
    assert repeat_string("abc", 3) == "abcabcabc"
