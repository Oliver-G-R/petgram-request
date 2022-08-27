import faker
fake = faker.Faker([
    'en_US',
])


def create_user():
    raza_dog = ['Labrador', 'Pitbull', 'Bulldog', 'Poodle', 'Husky',
                'Golden Retriever', 'Chihuahua', 'Pug', 'Beagle', 'Boxer']
    return {
        "nickname": fake.name()
        .lower()
        .replace(' ', ''),
        "name": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(),
        "birthday": fake.date(),
        "raza": raza_dog[fake.random_int(min=0, max=len(raza_dog) - 1)],
        "sexo": fake.random_element(elements=('Masculino', 'Femenino')),
        "phoneNUmber": fake.phone_number(),
    }
