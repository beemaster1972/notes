from abc import ABC, abstractmethod

class Operation(ABC):

    @abstractmethod
    def operation(self, *args, **kwargs):
        pass
