from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(): 
        pass

    def getName(self):
        return self.name