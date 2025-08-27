"""
Clases base abstractas para el patrón Observer y
diferentes displays de la estación meteorológica.
"""

from abc import ABC, abstractmethod


class Subject(ABC):
    """
    Clase base abstracta para los sujetos en el patrón Observer.
    """
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Observer(ABC):
    """
    Clase base abstracta para los observadores en el patrón Observer.
    """
    @abstractmethod
    def update(self):
        pass


class DisplayElement(ABC):
    """
    Clase base abstracta para los elementos de display de
    la estación meteorológica.
    """
    @abstractmethod
    def display(self):
        pass
