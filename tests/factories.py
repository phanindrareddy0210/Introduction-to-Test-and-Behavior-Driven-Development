from factory import Factory, Faker

class ProductFactory(Factory):
    class Meta:
        model = dict

    id = Faker('random_int', min=1, max=9999)
    name = Faker('word')
    category = Faker('word')
    available = Faker('boolean')
