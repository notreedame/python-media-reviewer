import pytest
from main import date_validation, rating_validation, non_empty_string_validation, language_validation

#unit tests for input validation functions
def test_date_validation_valid():
    assert date_validation("2024-05-12") == True

def test_date_validation_invalid():
    assert date_validation("2024/05/12") == False

def test_rating_validation_valid():
    assert rating_validation("7") == True

def test_rating_validation_invalid():
    with pytest.raises(ValueError):
        rating_validation("15")

def test_non_empty_string_validation():
    assert non_empty_string_validation("Book Title") == True
    with pytest.raises(ValueError):
        non_empty_string_validation("   ")

def test_language_validation_valid():
    assert language_validation("English") == True

def test_language_validation_invalid():
    with pytest.raises(ValueError):
        language_validation("123")