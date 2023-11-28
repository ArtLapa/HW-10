
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def validate(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Phone should be 10 digits')
            super().validate(value)
    def is_valid_phone(self, value):
        """return boolean from check"""
        return value.isdigit() and len(value) == 10

    def __init__(self, value):
            self.validate(value)
            super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def is_valid_phone(self, value):
        """return boolean from check"""
        return value.isdigit() and len(value) == 10

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)


    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError(f"Phone number '{old_phone}' not found")
    def remove_phone(self, phone):
        for record_phone in self.phones:
            try:
                record_phone.value == phone
                self.phones.remove(record_phone)
                return True
            except ValueError:
                return f'{phone} does not exist'


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None
    def delete(self, name):
        if name in self.data:
            del self.data[name]



if __name__ == '__main__':
    book = AddressBook()
        # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
        # Додавання запису John до адресної книги
    book.add_record(john_record)
        # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
        # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)
        # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
        # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
        # Видалення запису Jane
    book.delete("Jane")
    print(book)