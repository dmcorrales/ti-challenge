import random

from src.models.Person import Person


class Employee(Person):

    def __init__(self):
        super().__init__("Aaron", "Swartz", "aswartz@gmail.com")

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def is_active(self):
        return random.choice([True, False])
