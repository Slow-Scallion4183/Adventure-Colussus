import pytest
from random import randint, seed
from mock import patch
import builtins
import sys
from unittest.mock import mock_open
import adventure_colussus as ac
from functools import wraps

seed(20)

def mock_input_dec(options):
    def outer(func):
        def middle(*args, **kwargs):
            # input_values = ["1"]
            def wrapper(s="p"):
                return options.pop()
            ac.input = wrapper
            return func(*args, **kwargs)
        return middle
    return outer


@mock_input_dec(["1"])
def test_get_input():
    assert ac.get_input("Pick", ["1","2"]) == '1'       


@mock_input_dec(["1"])
def test_get_input_false():
    assert ac.get_input("Pick", ["1","2"]) != '2'


def test_session_counter():
    # tmp_path fixture?
    pass


def test_debug_print():
    pass


def test_print_text(capsys):
    ac.print_text("Test text")
    out, _ = capsys.readouterr()
    sys.stdout.write(out)
    assert out == "Test text"

    
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


# TODO Needs more
@mock_input_dec(["1"])
def test_character_style_menu_brawler():
    assert ac.character_style_menu() == ("Brawler", 100, 75)


@mock_input_dec(["2"])
def test_character_style_menu_ranger():
    assert ac.character_style_menu() == ("Ranger", 75, 50)


# TODO
# @mock_input_dec(["3"]
# def test_character_style_menu_ranger():
#     assert ac.character_style_menu() == Error


# TODO needs more
@mock_input_dec(["2"])
def test_attack_style_menu_brawler():
    assert ac.attack_style_menu() == (75,45)


@mock_input_dec(["1"])
def test_attack_style_menu_ranger():
    assert ac.attack_style_menu() == (50, 75)


# TODO
# @mock_input_dec(["3"]
# def test_character_style_menu_ranger():
#     assert ac.character_style_menu() == Error    

# @mock_input_dec(["1"])
# def test_luck_dec():
#     response = ac.luck_menu()
#     assert response == 2


@mock_input_dec(["Aragorn"])
def test_get_player_name():
    response = ac.get_player_name()
    assert response == "Aragorn"
    

@mock_input_dec([" "])
def test_get_player_name_no_name():
    response = ac.get_player_name()
    assert response != "Aragorn"
    

def test_add_player_choices():
    # TODO build character_dick mock
    pass
    
    
def test_character_generator():
    pass
    

def test_main_menu():
    pass

def test_new_character():
    pass

# @mock_input_dec(["tgimli"])
# def test_load_character():
#     with patch.object(builtins, 'input', lambda _: 'tgimli'):
#         assert type(ac.load_character('clear')[0]) == ac.entities.Human



#spacer
'''

def test_get_input():
    with patch.object(builtins, 'input', lambda _: '1'):
        assert ac.get_input("Pick", ["1","2"]) == '1'

def test_load_character_other():
    def mock_input(s):
        input_values = ['tgimli']
        return input_values.pop(0)
    ac.input = mock_input
    assert type(ac.load_character('clear')[0]) == ac.entities.Human

    '''