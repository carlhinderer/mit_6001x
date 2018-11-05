import pytest
import src.problem_set_1 as ps1


def test_count_vowels():
    assert ps1.count_vowels('') == 0
    assert ps1.count_vowels('bcd') == 0
    assert ps1.count_vowels('abc') == 1
    assert ps1.count_vowels('abcdefghijklm') == 3


def test_count_bobs():
    assert ps1.count_bobs('') == 0
    assert ps1.count_bobs('abcdefg') == 0
    assert ps1.count_bobs('abcbobdef') == 1
    assert ps1.count_bobs('bobob') == 2


def test_longest_alphabetic_substr():
    assert ps1.longest_alphabetic_substr('') == ''
    assert ps1.longest_alphabetic_substr('abc') == 'abc'
    assert ps1.longest_alphabetic_substr('abcbgastuvwllap') == 'stuvw'
    assert ps1.longest_alphabetic_substr('abcblthgnztuv') == 'abc'
