from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, first_name="Daniel",
                 last_name="Corrales",
                 email="danieldmc123@hotmail.com"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_full_name(self):
        pass

    @abstractmethod
    def is_active(self):
        pass
