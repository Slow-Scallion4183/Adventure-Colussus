import pytest
from .test_utils import mock_input_decorator
import adventure_colussus as ac



# TODO Figure out how to test this??
def test_main_main():
    response = ac.__main__.main()
    assert response == "1"    



'''
nb: entity.load()

my_text = "some text to return when read() is called on the file object"
mocked_open_function = mock.mock_open(read_data=my_text)

with mock.patch("__builtin__.open", mocked_open_function):
    with open("any_string") as f:
        print f.read()



'''



