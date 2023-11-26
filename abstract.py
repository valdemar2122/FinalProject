from abc import ABC, abstractmethod
import re
from datetime import datetime as dt

class BotView(ABC):
    @abstractmethod
    def display_content(data):
        print(data)


class Field():
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def abstract_print(self):
        return f"Name: {self.value}"
    
    def __str__(self):
        return f"Name: {self.value}"

class Phone(Field):

    def __init__(self, value=''):
        
        self.value = []
        if value:
            self.values = value
        else:
            self.values = input("Phones(+48......... or +38..........) (multiple phones can be added with space between them. +48 pattern has 9 symbols after code): ")
        try:
            for number in self.values.split(' '):
                if re.match('^\+48\d{9}$', number) or re.match('^\\+38\d{10}$', number) or number == '':
                    self.value.append(number)
                else:
                    raise ValueError
        except ValueError:
            print('Incorrect phone number format! Please provide correct phone number format.')
           

    def __getitem__(self):
        return self.value


class Birthday(Field):

    def __init__(self, value=''):
       
        if value:
            self.value = value
        else:
            self.value = input("Birthday date(dd/mm/YYYY): ")
        try:
            if re.match('^\d{2}/\d{2}/\d{4}$', self.value):
                self.value = dt.strptime(self.value.strip(), "%d/%m/%Y")
                pass
            elif self.value == '':
                pass
            else:
                raise ValueError
        except ValueError:
            print('Incorrect date! Please provide correct date format.')

    def __getitem__(self):
        return self.value


class Email(Field):

    def __init__(self, value=''):
    

        if value:
            self.value = value
        else:
            self.value = input("Email: ")
        try:
            if re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', self.value) or self.value == '':
                pass
            else:
                raise ValueError
        except ValueError:
            print('Incorrect email! Please provide correct email.')

    def __getitem__(self):
        return self.value


class Status(Field):

    def __init__(self, value=''):
        
        self.status_types = ['', 'family', 'friend', 'work']
        if value:
            self.value = value
        else:
            self.value = input("Type of relationship (family, friend, work): ")
        try:
            if self.value in self.status_types:
                pass
            else:
                raise ValueError
        except ValueError:
            print('There is no such status!')

    def __getitem__(self):
        return self.value


class Note(Field):
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value


if __name__ == "__main__":
    john = Name("John")
    BotView.display_content(john)

    john_phone = Phone("+389933445562")
    BotView.display_content(john_phone)

    john_birthday = Birthday("02/02/2000")
    BotView.display_content(john_birthday)

    john_email = Email("john@gmail.com")
    BotView.display_content(john_email)

    john_status = Status("friend")
    BotView.display_content(john_status)

    john_note = Note("He is my colleague")
    BotView.display_content(john_note)


