import pytest
from src.problem_set_3 import ps3_hangman


def test_isWordGuessed():
    word = 'testword'
    letters_guessed = ['t', 'e', 's', 'w', 'o', 'r', 'd']
    assert ps3_hangman.isWordGuessed(word, letters_guessed) == True

    letters_guessed = ['t', 'e', 's']
    assert ps3_hangman.isWordGuessed(word, letters_guessed) == False

    letters_guessed = []
    assert ps3_hangman.isWordGuessed(word, letters_guessed) == False


def test_getGuessedWord():
    word = 'testword'
    letters_guessed = ['t', 'e', 's', 'w', 'o', 'r', 'd']
    assert ps3_hangman.getGuessedWord(word, letters_guessed) == 'testword'

    letters_guessed = ['t', 's', 'w']
    assert ps3_hangman.getGuessedWord(word, letters_guessed) == 't _ stw _  _  _ '

    letters_guessed = []
    assert ps3_hangman.getGuessedWord(word, letters_guessed) == ' _  _  _  _  _  _  _  _ '
