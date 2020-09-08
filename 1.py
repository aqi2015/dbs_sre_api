class Dog:
    """A simple dog class"""
    def __init__(self, name):
        self._name = name
    def speak(self):
        return "Woof!"

class Cat:

    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):

    """The factory method"""

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]


def get_worker(worker, envparams):
    factory = dict(hive=Dog, alluxio=Cat)
    return factory.get(worker)(envparams)
    # d = factory.get(worker)(envparams)
    # print(dir(d))
    # print(d.speak())
    # d.speak()
    # print(factory.get(worker))
    # return factory.get(worker)(envparams)
    # return d


d = get_worker("hive", "dog")
print(d.speak())

d = get_worker("alluxio", "cat")
print(d.speak())

# d = get_pet("dog")
# ​
# print(d.speak())
# ​
# c = get_pet("cat")
# ​
# print(c.speak())
