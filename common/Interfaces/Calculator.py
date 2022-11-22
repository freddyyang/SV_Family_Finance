import abc


class CalculatorInterface(metaclass=abc.ABCMeta):
    """ Interface for calculators. """
    def __init__(self) -> None:
        #TODO: implement class
        pass

    @abc.abstractmethod
    def abstractfunc(self):
        pass
