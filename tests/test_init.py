import adventure_colussus.utils as ac
import pytest
from random import randint, seed
import mock
import builtins
import sys

def test_get_input():
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert ac.get_input("Pick", ["1","2"]) == '1'
        
def test_get_input_false():
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert ac.get_input("Pick", ["1","2"]) != '2'

def test_luck():
    with mock.patch.object(builtins, 'input', lambda _: ''):
        assert ac.luck_menu() == 100 

# def test_character_style_menu():
#     with mock.patch.object(ac.get_input, 'user_input', lambda _: '1'):
#         assert ac.get_input("Pick", ["1","2"]) != '2'


def test_print_text(capsys):
    ac.print_text("Test text")
    out, _ = capsys.readouterr()
    sys.stdout.write(out)
    assert out == "Test text"

'''
# why does this take so long to run??
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
'''

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

from unittest.mock import patch, mock_open

"""

def test_do_stuff_with_file():
    open_mock = mock_open()
    with patch("adventure_colossus.utils.open", open_mock, create=True):
        ac.session_counter("This is the session counter")

    open_mock.assert_called_with("output.txt", "w")
    open_mock.return_value.write.assert_called_once_with("This is the session counter")
"""