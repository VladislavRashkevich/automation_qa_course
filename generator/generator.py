import random
from data.data import Person, Color, Date, SelectValue
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('en')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )


def generated_file():

    path = rf'e:\python\automation_qa_course\filetest{random.randint(0, 999)}'
    file = open(path, "w+")
    file.write(f"Hello world{random.randint(0, 999)}")
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name=['Red',
                    'Blue',
                    'Green',
                    'Yellow',
                    'Purple',
                    'Black',
                    'White',
                    'Indigo',
                    'Magenta',
                    'Aqua'
        ]
    )


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:00",
    )


def generate_select_menu_value():
    yield SelectValue(
        list_values=['Group 1, option 1',
                      'Group 1, option 2',
                      'Group 2, option 1',
                      'Group 2, option 2',
                      'A root option',
                      'Another root option']
    )