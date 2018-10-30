import pytest
import src.problem_set_1 as ps1


def test_vowel_count():
    assert ps1.count_vowels('') == 0
    assert ps1.count_vowels('bcd') == 0
    assert ps1.count_vowels('abc') == 1
    assert ps1.count_vowels('abcdefghijklm') == 3
