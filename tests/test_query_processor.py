import pytest

from literature_searcher.query_processor import process

def test_returns_empty_string_on_invalid_query():
    assert process("") == []

def test_knows_about_shakespeare():
    assert any("playwright" in result for result in process("Shakespeare"))

def test_knows_about_asimov():
    assert any("science fiction" in result for result in process("Asimov"))

def test_not_case_sensitive():
    assert any("playwright" in result for result in process("shakespeare"))

def test_knows_about_ford():
    assert any("automaker" in result for result in process("Ford"))

def test_knows_about_tesla():
    assert any("electric vehicle" in result for result in process("Tesla"))

def test_knows_about_kant():
    assert any("German philosopher" in result for result in process("Kant"))

def test_knows_about_kia():
    assert any("automotive" in result for result in process("Kia"))
