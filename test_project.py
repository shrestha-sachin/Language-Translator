import pytest
from project import translate_text, validate_language_code, get_supported_languages, save_to_file, download_file
import os


def test_translate_text():
    assert translate_text('Hello', 'fr') == "Bonjour"
    assert translate_text('Goodbye', 'es') == "Adiós"
    assert translate_text('Python', 'de') == "Python"
    assert translate_text('Python is fun!', 'es') == "¡Python es divertido!"


def test_validate_language_code():
    assert validate_language_code('en') == True
    assert validate_language_code('fr') == True
    assert validate_language_code('ne') == True
    assert validate_language_code('es') == True
    assert validate_language_code('EN') == True
    assert validate_language_code('gys') == False
    assert validate_language_code('sdf') == False

def test_get_supported_languages():
    supported_languages = get_supported_languages()
    assert len(supported_languages) > 0

def test_save_to_file(tmpdir):
    text = "This is a test text"
    file_name = save_to_file(text)
    assert os.path.exists(file_name)
    assert os.path.isfile(file_name)
    with open(file_name, 'r', encoding='utf-8') as file:
        assert file.read() == text

def test_download_file(tmpdir):
    file_name = os.path.join(tmpdir, "test_file.txt")
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("Test content")

    with open(file_name, 'r', encoding='utf-8') as file:
        assert file.read() == "Test content"
