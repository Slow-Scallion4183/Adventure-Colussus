'''
nb: entity.load()

my_text = "some text to return when read() is called on the file object"
mocked_open_function = mock.mock_open(read_data=my_text)

with mock.patch("__builtin__.open", mocked_open_function):
    with open("any_string") as f:
        print f.read()



'''



