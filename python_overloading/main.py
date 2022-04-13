
class parent(object):
    def __init__(self, something,something_else):
        self.something = something
        self.something_else = something_else
    def logger(func):
        def wrapper_function(*args, **kwargs):
            print("prequel_logging")
            func(*args,  **kwargs)
            print("sequel_logging")
        return wrapper_function

class child(parent):

    @parent.logger
    def __init__(self, something):
        super(child, self).__init__(something,"endlisch")

bob = child("erst")
print(f"{bob.something}_{bob.something_else}")













