import datetime
import pytest
from random import randint, seed
from mock import patch
import builtins
import sys
from unittest.mock import mock_open
import adventure_colussus as ac
from functools import wraps, partial
from .test_utils import mock_input_decorator

seed(20)


# def mock_input_decorator(func=None, options=None):  # <--- !!
#     if func == None:
#         return partial(mock_input_decorator, options)

#     @wraps(func)
#     def wrapped(*args, **kwargs):
#         opt = list(options)  # Fixes your other error perhaps?
#         def wrapper(s="p"):
#             return opt.pop()
#         ac.input = wrapper
#         return func(*args, **kwargs)
#     return wrapped


@mock_input_decorator(options=["1"])
def test_get_input():
    assert ac.get_input("Pick", ["1","2"]) == '1'       


@mock_input_decorator(options=["1"])
def test_get_input_false():
    assert ac.get_input("Pick", ["1","2"]) != '2'


def test_session_counter():
    # tmp_path fixture?
    pass

def test_debug_print():
    testargs = ""
    with patch.object(sys, 'argv', testargs):
        startime = datetime.datetime.utcnow()
        ac.print_text("This is a test string", 0.5)
        end = datetime.datetime.utcnow() - startime
        assert end.total_seconds() > 1

def test_debug_print_d():
    testargs = "-d"
    with patch.object(sys, 'argv', testargs):
        startime = datetime.datetime.utcnow()
        ac.print_text("This is a test string", 0.5)
        end = datetime.datetime.utcnow() - startime
        assert end.total_seconds() < 2

# TODO test value assignment inside debug_print decorator
def test_try_value():
    pass
    
# TODO fix DRY in debug_print, then this test unnecessary
def test_except_value():
    pass

# TODO test return of inner function wrapper to confirm assignment
def test_return_value():
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
@mock_input_decorator(options=["1"])
def test_character_style_menu_brawler():
    assert ac.character_style_menu() == ("Brawler", 100, 75)


@mock_input_decorator(options=["2"])
def test_character_style_menu_ranger():
    assert ac.character_style_menu() == ("Ranger", 75, 50)


# TODO
# @mock_input_decorator(["3"])
# def test_character_style_menu_ranger():
#     assert ac.character_style_menu() == Error


# TODO needs more
@mock_input_decorator(options=["2"])
def test_attack_style_menu_brawler():
    assert ac.attack_style_menu() == (75,45)


@mock_input_decorator(options=["1"])
def test_attack_style_menu_ranger():
    assert ac.attack_style_menu() == (50, 75)


# TODO
# @mock_input_decorator(["3"]
# def test_character_style_menu_ranger():
#     assert ac.character_style_menu() == Error    
    
@mock_input_decorator(options=["1"])
def test_luck_dec():
    response = ac.luck_menu()
    assert response == 10


@mock_input_decorator(options=["Aragorn"])
def test_get_player_name():
    response = ac.get_player_name()
    assert response == "Aragorn"
    

@mock_input_decorator(options=[" "])
def test_get_player_name_no_name():
    response = ac.get_player_name()
    assert response != "Aragorn"
    

def test_add_player_choices_Brawler(sample_Dict_Brawler):
    assert sample_Dict_Brawler.name == 'dict_Brawler'
def test_add_player_choices_Ranger(sample_Dict_Ranger):
    assert sample_Dict_Ranger.name == 'dict_Ranger'   
def test_add_player_choices_Human(sample_Dict_Human):
    assert sample_Dict_Human.name == 'dict_Human'  


# TODO need to test all steps of character_generator
def test_character_generator():
    pass

choices = ["tgimli", "Boromir", "1", "2", "1"]
@mock_input_decorator(options=choices)
def test_character_gen_2():
    response = ac.character_generator()
    # assert response == ("<Brawler Aragorn hp=500 lvl=1>", "tgimli.dat")
    assert response[0].__repr__() == "<Brawler Boromir hp=500 lvl=1>"

    
# TODO this should be covered by main menu
def test_mountain_range():
    response = ac.mountain_range()
    assert response == None
    
@mock_input_decorator(options=["1"])
def test_main_menu():
    response = ac.main_menu("clear")
    assert response == "1"

'''
@mock_input_decorator(options=["1"])
def test_main_menu_print_block(capsys):
    menu_text = {
        "> [1] Create new game\n\
        > [2] Load existing game\n\
        > [3] End game\n\
        > [4] Credits\n"
    }
    ac.main_menu("clear")
    out, _ = capsys.readouterr()
    sys.stdout.write(out)
    assert menu_text in out

'''

choices = ["tgimli", "Aragorn", "1", "1", "2"]
def test_new_character(options=choices):
    response = ac.new_character()
    assert response[0].__repr__() == "<Ranger Aragorn hp=500 lvl=1>"



@mock_input_decorator(options=["tgimli"])
def test_load_character():
    with patch.object(builtins, 'input', lambda _: 'tgimli'):
        assert type(ac.load_character('clear')[0]) == ac.entities.Human



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