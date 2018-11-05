import pytest
from src.problem_set_1 import string_utils


def test_count_vowels():
    assert string_utils.count_vowels('') == 0
    assert string_utils.count_vowels('bcd') == 0
    assert string_utils.count_vowels('abc') == 1
    assert string_utils.count_vowels('abcdefghijklm') == 3


def test_count_bobs():
    assert string_utils.count_bobs('') == 0
    assert string_utils.count_bobs('abcdefg') == 0
    assert string_utils.count_bobs('abcbobdef') == 1
    assert string_utils.count_bobs('bobob') == 2


def test_longest_alphabetic_substr():
    assert string_utils.longest_alphabetic_substr('') == ''
    assert string_utils.longest_alphabetic_substr('abc') == 'abc'
    assert string_utils.longest_alphabetic_substr('abcbgastuvwllap') == 'stuvw'
    assert string_utils.longest_alphabetic_substr('abcblthgnztuv') == 'abc'
