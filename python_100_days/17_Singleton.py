from functools import wraps


def singletonize(cls):
    """decoratro to wrap a class"""
    instances = {}

    @wraps(cls)
    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrap

#* Closure is used in the above

@singleton
class President():
    """President(singleton)"""
    pass
