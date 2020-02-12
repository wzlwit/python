from functools import wraps
from threading import Lock


def singletonize(cls):
    """thread safety singleton wrapper/decorator"""
    instances = {}
    locker = Lock()

    @wraps(cls)
    def wrap(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrap

#* Closure is used in the above
