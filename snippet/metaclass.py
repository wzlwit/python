###* whose instance is a class *###


class ListMetaclass(type):
    """ template for class, so it is derived from 'type' """
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
                    # args: self, class name, parent class, attributes list

class MyList(list, metaclass=ListMetaclass):
    # parent class: list
    pass


L = MyList()
L.add(1)    #* normal list does not have method: add()
print(L)
# [1]


""" ORM: Object Relational Mapping """
