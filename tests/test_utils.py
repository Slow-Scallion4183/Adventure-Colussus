import adventure_colussus as ac

def mock_input_decorator(options):
    def outer(func):
        opts = list(options)
        def middle(*args, **kwargs):
            def wrapper(s="p"):
                print(opts[-1])
                return opts.pop()
            ac.input = wrapper
            return func(*args, **kwargs)
        return middle
    return outer

