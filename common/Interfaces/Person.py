import abc


class PersonInterface(metaclass=abc.ABCMeta):
    """ Interface for person. """
    def __init__(self) -> None:
        #TODO: implement class
        pass

    @abc.abstractmethod
    def abstractfunc(self):
        pass
