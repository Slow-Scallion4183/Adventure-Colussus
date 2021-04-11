import pytest
from random import randint, seed
from mock import patch
import builtins
import sys
from unittest.mock import mock_open
import adventure_colussus as ac


def test_load_character():
    with patch.object(builtins, 'input', lambda _: 'tgimli'):
        assert type(ac.load_character('clear')[0]) == ac.entities.Human


def test_get_input():
    with patch.object(builtins, 'input', lambda _: '1'):
        assert ac.get_input("Pick", ["1","2"]) == '1'

        
def test_get_input_false():
    with patch.object(builtins, 'input', lambda _: '1'):
        assert ac.get_input("Pick", ["1","2"]) != '2'


def test_print_text(capsys):
    ac.print_text("Test text")
    out, _ = capsys.readouterr()
    sys.stdout.write(out)
    assert out == "Test text"


def test_luck():
    def mock_input(s):
        input_values = ["1"]
        return input_values.pop(0)
    ac.input = mock_input
    response = ac.get_input("Pick", ["1","2"])
    assert response == "1"

# def test_character_style_menu():
#     with patch.object(ac.get_input, 'user_input', lambda _: '1'):
#         assert ac.get_input("Pick", ["1","2"]) != '2'

# why does this take so long to run??

def test_load_character_other():
    def mock_input(s):
        input_values = ['tgimli']
        return input_values.pop(0)
    ac.input = mock_input
    assert type(ac.load_character('clear')[0]) == ac.entities.Human
def test_print_block(capsys):
    luck_text = {
        "\n > Good good! We have decided your play style and your preferred ways of attacking the enemy!\n": 0,
        " > Now, we must see what luck we are able to bestow upon you. Be warned: it is entirely random!\n": 0
    }
    ac.print_block(luck_text)
    out, _ = capsys.readouterr()
    sys.stdout.write(out)
    # assert out == "\n > Good good! We have decided your play style and your preferred ways of attacking the enemy!\n > Now, we must see what luck we are able to bestow upon you. Be warned: it is entirely random!\n"
    assert out.startswith("\n > Good good")

def test_session_counter():
    # tmp_path fixture?
    pass

# def test_result_and_stdout(capsys):
#     result = method_under_test()
#     out, err = capsys.readouterr()
#     sys.stdout.write(out)
#     sys.stderr.write(err)
#     assert out.startswith("Hello")
#     assert result == 42



#spacer
