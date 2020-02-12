import threading


class SingletonMeta(type):
    """customerized metaclass"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    """ singleton """
    pass